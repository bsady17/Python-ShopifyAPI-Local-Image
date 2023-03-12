# Base Modules
import shopify
import base64

# App/Store Data
shop_url = "STORE_URL.myshopify.com"
api_version = "2023-01" # 2023-01 is the current latest version as of March 12, 2023
api_key = "API_KEY"
api_password = "API_SECRET_PASSWORD"

# Add image paths
image_files = ["/Users/yourname/Downloads/image1.jpg", "/Users/yourname/Downloads/image2.jpg"]

# Start Shopify session
session = shopify.Session(shop_url, api_version, api_password)
shopify.ShopifyResource.activate_session(session)

# Create a new product with basic info
new_product = shopify.Product()
new_product.title = "New Title32746374"
new_product.price = "20.99"
new_product.body_html = "Product description"

# Save the product to create a product_id
new_product.save()

# Upload images to the product
for image_file in image_files:
    with open(image_file, 'rb') as f:
        image_data = f.read()

    # Encoding the image in base64 format is required
    image_data_b64 = base64.b64encode(image_data).decode('utf-8')
    new_image = shopify.Image({
        'product_id': new_product.id,
        'filename': image_file,
        'attachment': image_data_b64
    })
    new_image.save()

# End Shopify session
shopify.ShopifyResource.clear_session()