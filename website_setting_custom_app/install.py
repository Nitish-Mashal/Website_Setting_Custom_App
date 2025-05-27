# import frappe

# def toggle_website_settings(apply=True):
#     file_urls = {
#         "QB Logo.png": "/files/QB Logo.png",
#         "Q_Logo.png": "/files/Q_Logo.png"
#     }

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

#     ws = frappe.get_single("Website Settings")

#     if apply:
#         # On app install
#         for file_name, file_url in file_urls.items():
#             upload_file(file_name, file_url)

#         ws.app_logo = file_urls["QB Logo.png"]
#         ws.banner_image = file_urls["QB Logo.png"]
#         ws.splash_image = file_urls["Q_Logo.png"]
#         ws.favicon = file_urls["Q_Logo.png"]
#         ws.app_name = "Quantumberg Technologies Pvt Ltd"
#     else:
#         # On app uninstall
#         for file_url in file_urls.values():
#             existing = frappe.db.get_all("File", filters={"file_url": file_url})
#             for file in existing:
#                 frappe.delete_doc("File", file.name, force=True)

#         ws.app_logo = None
#         ws.banner_image = None
#         ws.splash_image = None
#         ws.favicon = None
#         ws.app_name = None

#     ws.save()
#     frappe.db.commit()


# def after_install():
#     toggle_website_settings(apply=True)

# def before_uninstall():
#     toggle_website_settings(apply=False)

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
        ws.favicon = file_urls["Q_Logo.png"]
        ws.app_name = "Quantumberg Technologies Pvt Ltd"

        # Add custom brand HTML
        # ws.brand_html = """
        # <a href="/app/home" style="display: flex; align-items: center;">
        #     <img src="/files/QB Logo.png" style="max-height: 30px;">
        # </a>

        # <style>
        # .navbar {
        #     display: flex;
        #     align-items: center;
        #     justify-content: space-between;
        #     padding: 8px;
        # }

        # .navbar a img {
        #     max-height: 40px;
        # }

        # .navbar .navbar-toggler {
        #     margin-left: auto;
        # }
        # </style>
        # """
    else:
        # On app uninstall
        for file_url in file_urls.values():
            existing = frappe.db.get_all("File", filters={"file_url": file_url})
            for file in existing:
                frappe.delete_doc("File", file.name, force=True)

        ws.app_logo = None
        ws.banner_image = None
        ws.splash_image = None
        ws.favicon = None
        ws.app_name = None
        # ws.brand_html = None

    ws.save()
    frappe.db.commit()


def after_install():
    toggle_website_settings(apply=True)

def before_uninstall():
    toggle_website_settings(apply=False)
