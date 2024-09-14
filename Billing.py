from PIL import Image, ImageDraw, ImageFont

# Prices of services
prices = {
    "hair_cut": 150,
    "beard": 100,
    "facial": 350,
    "massage": 500
}

# Shop name
shop_name = "TECH VISION SALON"

# User inputs
services_taken = []
print("Please select the services taken by the customer (type 'done' when finished):")
print("1. Hair Cut - 150 rupees")
print("2. Beard - 100 rupees")
print("3. Facial - 350 rupees")
print("4. Full Body Massage - 500 rupees")

while True:
    service = input("Enter service name (hair_cut, beard, facial, massage) or 'done': ").strip()
    if service == 'done':
        break
    if service in prices:
        services_taken.append(service)
    else:
        print("Invalid service name. Please try again.")

# Calculate total bill
total_bill = sum(prices[service] for service in services_taken)

# Bill details
bill_details = f"Total Bill Amount: {total_bill} rupees"

# Create an image for the bill
width, height = 400, 300
image = Image.new('RGB', (width, height), color = 'white')
draw = ImageDraw.Draw(image)

# Fonts
try:
    font_title = ImageFont.truetype("arial.ttf", 30)
    font_text = ImageFont.truetype("arial.ttf", 20)
except IOError:
    font_title = ImageFont.load_default()
    font_text = ImageFont.load_default()

# Draw text
draw.text((10, 10), shop_name, font=font_title, fill="black")
y = 60
for service in services_taken:
    draw.text((10, y), f"{service.replace('_', ' ').title()} - {prices[service]} rupees", font=font_text, fill="black")
    y += 30

draw.text((10, y + 10), bill_details, font=font_text, fill="black")

# Save the image
image.save('bill.png')

print(f"Bill generated successfully! Total amount: {total_bill} rupees. Check the file 'bill.png'.")