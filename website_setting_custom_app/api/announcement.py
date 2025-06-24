import frappe

def publish_announcement(doc, method):
    frappe.get_doc({
        "doctype": "Published Announcement",
        "title": doc.title,
        "description": doc.description,
        "created_date": doc.created_date or frappe.utils.nowdate()
    }).insert(ignore_permissions=True)