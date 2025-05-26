import frappe

def remove_website_logos():
    file_urls = [
        "/files/QB Logo.png",
        "/files/Q_Logo.png"
    ]

    # Delete logo files
    for file_url in file_urls:
        files = frappe.db.get_all("File", filters={"file_url": file_url})
        for file in files:
            frappe.delete_doc("File", file.name, force=True)

    # Clear logo fields in Website Settings
    ws = frappe.get_single("Website Settings")
    ws.app_logo = None
    ws.banner_image = None
    ws.splash_image = None

    ws.save()
    frappe.db.commit()
