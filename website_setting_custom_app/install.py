import frappe

def update_website_settings():
    # Upload logo if not already uploaded
    file_url = "/files/QB Logo.png"

    # Ensure file exists
    if not frappe.db.exists("File", {"file_url": file_url}):
        with open(frappe.get_app_path("your_app_name", "public", "files", "QB Logo.png"), "rb") as f:
            frappe.get_doc({
                "doctype": "File",
                "file_name": "QB Logo.png",
                "attached_to_doctype": None,
                "attached_to_name": None,
                "is_private": 0,
                "content": f.read(),
            }).insert(ignore_permissions=True)

    # Update Website Settings
    ws = frappe.get_single("Website Settings")
    ws.app_logo = file_url
    ws.save()

    frappe.db.commit()
