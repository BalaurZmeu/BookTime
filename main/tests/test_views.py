from django.test import TestCase
from django.urls import reverse
from main import forms


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
            response.context['form'], forms.ContactForm
        )

