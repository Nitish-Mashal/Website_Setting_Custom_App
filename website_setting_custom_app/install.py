# Use Frappe functions (like frappe.get_doc, frappe.get_app_path, etc.)
import frappe
# Use the OS module to check for file existence
import os

# Common files to be uploaded for branding and PWA
file_urls = {
    # Website branding files
    "QB_Logo.png": "/files/QB_Logo.png",
    "Q_Logo.png": "/files/Q_Logo.png",
    
    # PWA related files
    "manifest.json": "/files/manifest.json",
    "logo-512.png": "/files/logo-512.png",
    "logo-192.png": "/files/logo-192.png",
    "logo.svg": "/files/logo.svg",
}

manifest_link = '<link rel="manifest" href="/files/manifest.json">'


def upload_file(app_name, file_name, file_url):
    full_path = frappe.get_app_path(app_name, "public", "files", file_name)

    if not os.path.exists(full_path):
        frappe.throw(f"File not found: {full_path}")

    # Delete existing file if any
    existing = frappe.db.get_all("File", filters={"file_url": file_url})
    for file in existing:
        frappe.delete_doc("File", file.name, force=True)

    # Upload file
    with open(full_path, "rb") as f:
        frappe.get_doc({
            "doctype": "File",
            "file_name": file_name,
            "is_private": 0,
            "content": f.read(),
        }).insert(ignore_permissions=True)


def toggle_all_settings(apply=True):
    ws = frappe.get_single("Website Settings")
    head_html = ws.head_html or ""

    if apply:
        # Upload files from their respective apps
        branding_files = {
            "QB_Logo.png": "website_setting_custom_app",
            "Q_Logo.png": "website_setting_custom_app"
        }
        pwa_files = {
            "manifest.json": "website_setting_custom_app",
            "logo-512.png": "website_setting_custom_app",
            "logo-192.png": "website_setting_custom_app",
            "logo.svg": "website_setting_custom_app"
        }

        for file_name, app in {**branding_files, **pwa_files}.items():
            upload_file(app, file_name, file_urls[file_name])

        # Set branding
        ws.app_logo = file_urls["QB_Logo.png"]
        ws.banner_image = file_urls["QB_Logo.png"]
        ws.splash_image = file_urls["Q_Logo.png"]
        ws.favicon = file_urls["Q_Logo.png"]
        ws.app_name = "Quantumberg Technologies Pvt Ltd"

        ws.brand_html = """
        <a href="/app/home" style="display: flex; align-items: center;">
            <img src="/files/QB_Logo.png" style="max-height: 30px;">
        </a>

        <style>
        .navbar {
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 8px;
        }

        .navbar a img {
            max-height: 40px;
        }

        .navbar .navbar-toggler {
            margin-left: auto;
        }
        </style>
        """

        # Add PWA manifest link if not present
        if manifest_link not in head_html:
            ws.head_html = f"{head_html}\n{manifest_link}".strip()

    else:
        # Remove all files
        for file_url in file_urls.values():
            existing = frappe.db.get_all("File", filters={"file_url": file_url})
            for file in existing:
                frappe.delete_doc("File", file.name, force=True)

        # Reset branding
        ws.app_logo = None
        ws.banner_image = None
        ws.splash_image = None
        ws.favicon = None
        ws.app_name = None
        ws.brand_html = None

        # Remove manifest link
        if manifest_link in head_html:
            ws.head_html = head_html.replace(manifest_link, "").strip()

    ws.save()
    frappe.db.commit()


# Hooks
def after_install():
    toggle_all_settings(apply=True)

def before_uninstall():
    toggle_all_settings(apply=False)