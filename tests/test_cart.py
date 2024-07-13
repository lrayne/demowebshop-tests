from selene import browser, have
from demowebshop_tests.request import api_request, url
from demowebshop_tests.data import computers


def test_cart_should_have_computer_with_provided_attributes():

    # GIVEN
    computer = computers.computer
    data = {
        'product_attribute_72_5_18': computer.processor.value,
        'product_attribute_72_6_19': computer.ram.value,
        'product_attribute_72_3_20': computer.hdd.value,
    }

    # WHEN
    response = api_request(
        url, '/addproducttocart/details/72/1', method='POST', data=data
    )
    cookie = response.cookies.get('Nop.customer')

    # AND
    browser.open('/cart')
    browser.driver.add_cookie({'name': 'Nop.customer', 'value': cookie})
    browser.driver.refresh()

    # THEN
    browser.element('.cart').element('.product').element('.attributes').should(
        have.exact_text(
            f'Processor: {computer.processor.to_human_readable()} [+100.00]\n'
            f'RAM: {computer.ram.to_human_readable()}\n'
            f'HDD: {computer.hdd.to_human_readable()}'
        )
    )


def test_cart_should_display_correct_quantity_of_products():

    # GIVEN
    quantity_to_buy = '5'

    data = {
        'addtocart_31.EnteredQuantity': quantity_to_buy,
    }

    # WHEN
    response = api_request(
        url, '/addproducttocart/details/31/1', method='POST', data=data
    )
    cookie = response.cookies.get('Nop.customer')

    # AND
    browser.open('/cart')
    browser.driver.add_cookie({'name': 'Nop.customer', 'value': cookie})
    browser.driver.refresh()

    # THEN
    browser.element('.cart').element('.cart-item-row').element('.qty-input').should(
        have.value(quantity_to_buy)
    )


def test_remove_product_from_cart():

    # WHEN
    response = api_request(url, '/addproducttocart/details/13/1', method='POST')

    cookie = response.cookies.get('Nop.customer')

    # AND
    browser.open('/cart')
    browser.driver.add_cookie({'name': 'Nop.customer', 'value': cookie})
    browser.driver.refresh()
    pass

    browser.element('.cart').element('[name=removefromcart]').click()
    browser.element('[name=updatecart]').click()
    browser.element('.order-summary-content').should(
        have.exact_text('Your Shopping Cart is empty!')
    )
