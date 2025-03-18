from django.shortcuts import render
from django.forms import formset_factory
from django.http import HttpResponse, FileResponse
from .forms import InvoiceForm, ItemForm, addressform
from fpdf import FPDF
import os
from . import pdf
from datetime import date


def generate_pdf(request):
    ItemFormSet = formset_factory(ItemForm, extra=1)
    addform = addressform()
    form = InvoiceForm()
    formset = ItemFormSet()
    if request.method == "POST":
        addform = addressform(request.POST)
        form = InvoiceForm(request.POST)
        formset = ItemFormSet(request.POST)
        if form.is_valid() and formset.is_valid() and addform.is_valid():
            customer_detail = form.cleaned_data["customer_number"]
            # line1 = request.POST.get("address", "")
            # print(f"Extracted Address: {line1}")  #  Debugging step
            address = []
            for addrss in addform:
                organization_name = request.POST.get("org_name", "")
                line1 = request.POST.get("line1", "")
                line2 = request.POST.get("line2", "")
                line3 = request.POST.get("line3", "")

                address.append((organization_name, line1, line2, line3))
            items = []
            print("Uploaded Files:", request.FILES)
            for item_form in formset:
                if item_form.cleaned_data:
                    item_name = item_form.cleaned_data["name"]
                    item_description = item_form.cleaned_data["description"]
                    item_qty = item_form.cleaned_data["qty"]
                    item_price = item_form.cleaned_data["price"]
                    items.append((item_name, item_description, item_qty, item_price))
            pdf_file_name = f"{customer_detail}_{date.today()}_bill.pdf"
            # print(f"before passing {line1}")
            pdf.main(customer_detail, items, address)
            pdf_path = os.path.join(
                os.path.dirname(__file__), "static", "invoices", pdf_file_name
            )
            if not os.path.exists(pdf_path):
                return render(
                    request,
                    "invoice_form.html",
                    {"error": "PDF file was not generated."},
                )

            return FileResponse(open(pdf_path, "rb"), content_type="application/pdf")

    return render(
        request,
        "invoice_form.html",
        {"addform": addform, "form": form, "formset": formset},
    )
