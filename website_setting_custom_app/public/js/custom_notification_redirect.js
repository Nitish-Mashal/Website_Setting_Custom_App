// frappe.desktop.original_show_notification = frappe.desktop.show_notification;

// frappe.desktop.show_notification = function (log) {
//     frappe.call({
//         method: "website_setting_custom_app.api.custom_log.get_custom_log_for_notification",
//         args: { notification_log: log.name },
//         callback: function (r) {
//             if (r.message && r.message.name) {
//                 frappe.set_route("Form", "Custom Notification Log", r.message.name);
//             } else {
//                 frappe.desktop.original_show_notification(log);
//             }
//         }
//     });
// };


frappe.desktop.original_show_notification = frappe.desktop.show_notification;

frappe.desktop.show_notification = function (log) {
    if (log.document_type === "Event" || log.document_type === "Notification Log") {
        window.location.href = `/custom-notification-view?doctype=${log.document_type}&name=${log.document_name}`;
    } else {
        frappe.desktop.original_show_notification(log);
    }
};
