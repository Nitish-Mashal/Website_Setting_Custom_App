# import frappe

# # For Notification Log
# def create_log_from_notification(doc, method):
#     frappe.get_doc({
#         "doctype": "Custom Notification Log",
#         "subject": doc.subject or "No Subject",
#         "description": doc.message or "", 
#         "reference_doctype": "Notification Log",
#         "reference_name": doc.name
#     }).insert(ignore_permissions=True)

# # For Event
# def create_log_from_event(doc, method):
#     if doc.event_type == "Public":  
#         frappe.get_doc({
#             "doctype": "Custom Notification Log",
#             "subject": doc.subject or "Event Notification",
#             "description": doc.description or "",
#             "reference_doctype": "Event",
#             "reference_name": doc.name
#         }).insert(ignore_permissions=True)



# @frappe.whitelist()
# def get_custom_log_for_notification(notification_log):
#     log = frappe.get_all("Custom Notification Log",
#         filters={"reference_doctype": "Notification Log", "reference_name": notification_log},
#         fields=["name"],
#         limit=1
#     )
#     return log[0] if log else None
