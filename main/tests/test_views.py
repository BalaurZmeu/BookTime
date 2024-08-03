from django.test import TestCase
from django.urls import reverse
from decimal import Decimal
from main import forms, models


class TestPage(TestCase):
    def test_home_page_works(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/home.html')
        self.assertContains(response, 'BookTime')
        self.assertContains(response, 'Home')
        
    def test_about_us_page_works(self):
        response = self.client.get(reverse('about_us'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/about_us.html')
        self.assertContains(response, 'BookTime')
        self.assertContains(response, 'About us')
    
    def test_contact_us_page_works(self):
        response = self.client.get(reverse('contact_us'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/contact_form.html')
        self.assertContains(response, 'BookTime')
        self.assertContains(response, 'Contact us')
        self.assertIsInstance(
            response.context['form'], forms.ContactForm)

    def test_products_page_returns_active(self):
        models.Product.objects.create(
            name='The cathedral and the bazaar',
            slug='cathedral-bazaar',
            price=Decimal('10.00'))
        models.Product.objects.create(
            name='A Tale of Two Cities',
            slug='tale-two-cities',
            price=Decimal('2.00'),
            active=False)
        response = self.client.get(
            reverse('products', kwargs={'tag': 'all'}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'BookTime')
        
        active_products = models.Product.objects.active().order_by(
            'name')
        self.assertEqual(
            list(response.context['object_list']),
            list(active_products))
