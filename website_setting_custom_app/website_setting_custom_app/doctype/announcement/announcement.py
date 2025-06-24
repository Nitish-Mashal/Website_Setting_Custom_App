from frappe.website.website_generator import WebsiteGenerator
import frappe

class Announcement(WebsiteGenerator):
    def get_context(self, context):
        context.template = "templates/generators/announcement.html"
        context.doc = self
