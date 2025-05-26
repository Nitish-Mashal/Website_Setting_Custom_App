# import frappe

# def update_website_settings():
#     file_url = "/files/QB Logo.png"
#     file_url_Q_Logo = "/files/Q_Logo.png"

#     file_name = "QB Logo.png"
#     file_name_Q = "Q_Logo.png"

#     # Upload function to avoid repetition
#     def upload_file(file_name, file_url):
#         full_path = frappe.get_app_path("website_setting_custom_app", "public", "files", file_name)

#         # Delete existing file
#         existing = frappe.db.get_all("File", filters={"file_url": file_url})
#         for file in existing:
#             frappe.delete_doc("File", file.name, force=True)

#         # Upload new file
#         with open(full_path, "rb") as f:
#             frappe.get_doc({
#                 "doctype": "File",
#                 "file_name": file_name,
#                 "attached_to_doctype": None,
#                 "attached_to_name": None,
#                 "is_private": 0,
#                 "content": f.read(),
#             }).insert(ignore_permissions=True)

#     # Upload the three logos
#     upload_file(file_name, file_url)
#     upload_file(file_name_Q, file_url_Q_Logo)

#     # Update Website Settings
#     ws = frappe.get_single("Website Settings")
#     ws.app_logo = file_url
#     ws.banner_image = file_url
#     ws.splash_image = file_url_Q_Logo

#     ws.save()
#     frappe.db.commit()

import frappe

def toggle_website_settings(apply=True):
    file_urls = {
        "QB Logo.png": "/files/QB Logo.png",
        "Q_Logo.png": "/files/Q_Logo.png"
    }

    def upload_file(file_name, file_url):
        full_path = frappe.get_app_path("website_setting_custom_app", "public", "files", file_name)

        # Delete existing file
        existing = frappe.db.get_all("File", filters={"file_url": file_url})
        for file in existing:
            frappe.delete_doc("File", file.name, force=True)

        # Upload new file
        with open(full_path, "rb") as f:
            frappe.get_doc({
                "doctype": "File",
                "file_name": file_name,
                "attached_to_doctype": None,
                "attached_to_name": None,
                "is_private": 0,
                "content": f.read(),
            }).insert(ignore_permissions=True)

    ws = frappe.get_single("Website Settings")

    if apply:
        # On app install
        for file_name, file_url in file_urls.items():
            upload_file(file_name, file_url)

        ws.app_logo = file_urls["QB Logo.png"]
        ws.banner_image = file_urls["QB Logo.png"]
        ws.splash_image = file_urls["Q_Logo.png"]
        ws.app_name = "Quantumberg Technologies Pvt Ltd"
    else:
        # On app uninstall
        for file_url in file_urls.values():
            existing = frappe.db.get_all("File", filters={"file_url": file_url})
            for file in existing:
                frappe.delete_doc("File", file.name, force=True)

        ws.app_logo = None
        ws.banner_image = None
        ws.splash_image = None
        ws.app_name = None

    ws.save()
    frappe.db.commit()


def after_install():
    toggle_website_settings(apply=True)

def before_uninstall():
    toggle_website_settings(apply=False)

