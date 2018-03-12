from django.test import TestCase
from contacts.models import Contact


class ContactTest(TestCase):
    """
        Testing the Contact model
    """

    def setUp(self):
        Contact.objects.create(
            name="Vubon Roy",
            mobile="01737388296",
            age=200
        )

        Contact.objects.create(
            name="Sharif",
            mobile="01737573157",
            age=100
        )

    def test_person_name(self):
        contact_vubon = Contact.objects.get(name='Vubon Roy')
        contact_sharif = Contact.objects.get(name="Sharif")

        self.assertEqual(
            contact_vubon.person_name(), "Vubon Roy owner of this mobile 01737388296"
        )

        self.assertEqual(
            contact_sharif.person_name(), "Sharif owner of this mobile 01737573157"
        )
