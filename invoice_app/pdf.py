from fpdf import FPDF
from datetime import datetime, date
import os


class FPDF(FPDF):
    def header(self):
        pass

    def footer(self):
        self.set_font("Arial", "I", 10)
        self.set_y(-15)
        self.cell(
            0,
            10,
            "Developed by ASR",
            align="C",
            link="https://github.com/ankushsinghrajput-git",
        )
        pageNum = self.page_no()
        self.cell(0, 10, str(pageNum), align="R")


# class Items:
#     def __init__(self, name, description, qty: int, price: float):
#         self.name = name
#         self.description = description
#         self.qty = qty
#         self.price = price


# pdf = FPDF()

# # settings change
# # items = input("Total items: ")
# pdf.set_font("Arial", size=10)
# pdf.add_page()
# pdf.image("zudio.png", w=60)
# pdf.set_xy(70, 25)
# organization_name = "Zudio"
# address1 = "Elan Miracle Mall"
# address2 = "Sector 86, Dwarka Expressway"
# pincode = "Gurugram, Haryana, 122001"
# if items == "1163":
#     organization_name = input("New name: ")
# pdf.multi_cell(
#     0,
#     5,
#     f"{organization_name}, \n{address1} \n{address2} \n{pincode}",
#     align="R",
# )
# pdf.set_font("Arial", "B", size=18)
# n = 80
# pdf.set_y(n)
# pdf.cell(0, 10, "TAX INVOICE", align="C")
# pdf.set_font("Arial", size=10)

# pdf.set_y(n + 30)
# # customer_detail = input("Customer Number: ")
# customer_detail = 7568792205
# pdf.cell(0, 10, f"Customer Details - {customer_detail}")


# # item table
# pdf.set_font("Arial", style="B")
# pdf.set_y(n + 50)
# pdf.cell(50, 10, "Item Name", align="C")
# pdf.cell(80, 10, "Description", align="C")
# pdf.cell(25, 10, "Qty", align="C")
# pdf.cell(35, 10, "Price", align="C")


# # Items
# pdf.set_font("Arial", style="I")
# total_qty = 0
# total_price = 0
# n = n + 60
# items = 0
# for i in range(int(items)):
#     if items == "1163":
#         break
#     item_name = input("Item Name: ")
#     item_description = input("Item description: ")
#     item_qty = int(input("Item qty: "))
#     item_price = float(input("Item_price: "))
#     cartitem = Items(item_name, item_description, item_qty, item_price)
#     n = n + 10
#     pdf.set_y(n)
#     pdf.cell(50, 10, cartitem.name, align="C")
#     pdf.cell(80, 10, cartitem.description, align="C")
#     pdf.cell(25, 10, str(cartitem.qty), align="C")
#     pdf.cell(35, 10, str(float(cartitem.price)), align="C")

#     total_qty = total_qty + item_qty
#     total_price = total_price + item_price


# # total
# pdf.set_font("Arial")
# pdf.set_xy(-70, n + 20)
# pdf.cell(25, 10, str(total_qty), align="C")
# pdf.cell(35, 10, str(total_price), align="C")
# pdf.set_x(10)
# pdf.cell(20, 10, "Gross Total", align="C")
# pdf.set_xy(10, n + 40)
# pdf.cell(50, 10, f"Total: {total_price}", ln=1)
# pdf.cell(50, 10, f"No. of items: {total_qty}", ln=1)
# pdf.line(23, n, 191, n)

# time = datetime.now()
# # pdf.output(f"{customer_detail}_{date.today()}_bill.pdf")
# pdf.output("example.pdf")

# # print(f"{date.today()}_{datetime.now().strftime('%H:%M:%S')}_bill")


def main(details: str, items: list, address: list):
    global pdf
    pdf = FPDF()
    pdf.set_font("Arial", size=10)
    pdf.add_page()
    # pdf.image("logo.jpg", w=60)
    pdf.set_y(40)

    for name, line1, line2, line3 in address:
        organization_name = name
        address1 = line1
        address2 = line2
        pincode = line3

    address_text = f"{address1} \n{address2} \n{pincode}"
    address_text = address_text.encode("utf-8", "ignore").decode("utf-8")
    pdf.multi_cell(0, 5, address_text, align="C")
    pdf.set_line_width(0.4)
    pdf.line(53, 60, 161, 60)
    pdf.set_font("Arial", "B", size=18)
    pdf.set_y(30)
    pdf.cell(0, 10, organization_name, align="C")
    n = 80
    pdf.set_y(n)
    pdf.set_font("Arial", "B", size=24)

    pdf.cell(0, 10, "TAX INVOICE", align="C")
    pdf.set_font("Arial", size=10)

    pdf.set_y(n + 30)
    # customer_detail = input("Customer Number: ")
    customer_detail = details
    pdf.cell(0, 10, f"Customer Details - {customer_detail}")

    # item table
    pdf.set_font("Arial", style="B")
    pdf.set_y(n + 50)
    pdf.cell(30, 10, "Item Name", align="C")
    pdf.cell(65, 10, "Description", align="C")
    pdf.cell(20, 10, "Qty", align="C")
    pdf.cell(20, 10, "Rate", align="C")
    pdf.cell(20, 10, "Tax", align="C")

    pdf.cell(35, 10, "Price", align="C")

    # Items
    pdf.set_font("Arial", style="I")
    total_qty = 0
    total_price = 0
    total_tax = 0
    total_rate = 0
    n = n + 60
    # items = 1
    for item_name, item_description, item_qty, item_price in items:
        n = n + 10
        pdf.set_y(n)
        pdf.cell(30, 10, item_name, align="C")
        pdf.cell(65, 10, item_description, align="C")
        pdf.cell(20, 10, str(item_qty), align="C")
        rate = "{:.2f}".format(item_price - (item_price * 0.09))
        pdf.cell(20, 10, str(float(rate)), align="C")
        tax = "{:.2f}".format(item_price * 0.09)
        pdf.cell(20, 10, str(float(tax)), align="C")
        print(item_price * item_qty)
        price = item_price * item_qty
        pdf.cell(35, 10, str(float(price)), align="C")
        pdf.ln()
        total_rate += float(rate)
        total_tax += float(tax)
        total_qty += item_qty
        total_price += price
    # total
    l = 140 + 10
    pdf.set_font("Arial")
    pdf.set_xy(-105, n + 20)
    pdf.cell(20, 10, str(total_qty), align="C")
    pdf.cell(20, 10, str(total_rate), align="C")
    pdf.cell(20, 10, str(total_tax), align="C")
    pdf.cell(35, 10, str(total_price), align="C")
    pdf.set_x(10)
    pdf.cell(20, 10, "Gross Total", align="C")
    pdf.set_xy(10, n + 40)
    pdf.cell(50, 10, f"Total: {total_price}", ln=1)
    pdf.cell(50, 10, f"No. of items: {total_qty}", ln=1)
    pdf.set_line_width(0.1)
    pdf.line(23, 145, 191, 145)

    pdf.cell(
        10,
        10,
    )

    output_dir = os.path.join(os.path.dirname(__file__), "static", "invoices")
    os.makedirs(output_dir, exist_ok=True)

    # Save PDF to the correct directory
    file_name = f"{customer_detail}_{date.today()}_bill.pdf"
    output_path = os.path.join(output_dir, file_name)
    pdf.output(output_path)
    print(f"PDF saved to: {output_path}")


if __name__ == "__main__":
    main()
