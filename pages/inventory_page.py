from playwright.sync_api import Page

class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        self.inventory_list = ".inventory_list" 
        self.add_item_to_cart = "button[data-test^='add-to-cart-sauce-labsbackpack']"
        self.cart_icon = "a.shopping_cart_link"
        self.cart_badge = ".shopping_cart_badge"
        # self.product_title = "span[data-test='product_title']"
  

    def is_loaded(self):
        return self.page.locator(self.inventory_list).is_visible()
    
    def add_first_item_to_cart(self):
        # self.page.click(self.add_to_cart_btn)
        self.page.locator(self.add_to_card_btn).click()

    def open_to_cart(self):
        self.page.click(self.cart_icon)

    def items_in_card(self):
        if self.page.locator(self.cart_badge).is_visible():
            return int(self.page.locator(self.cart_badge).text_content())
        return 0

