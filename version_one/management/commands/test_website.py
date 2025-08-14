from django.core.management.base import BaseCommand
from django.test import Client
from django.urls import reverse
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = "Test all website pages and functionality"

    def add_arguments(self, parser):
        parser.add_argument(
            "--verbose",
            action="store_true",
            help="Show detailed output",
        )

    def handle(self, *args, **options):
        self.verbose = options["verbose"]
        self.client = Client()

        self.stdout.write("🚀 Testing website pages and functionality...\n")

        # Test basic pages
        self.test_basic_pages()

        # Test property filtering
        self.test_property_filtering()

        # Test pagination
        self.test_pagination()

        self.stdout.write(self.style.SUCCESS("\n✅ All tests completed!"))

    def test_url(self, url, description):
        """Test a specific URL"""
        try:
            response = self.client.get(url)
            if response.status_code == 200:
                self.stdout.write(f"✅ {description}: {url}")
                if self.verbose:
                    self.stdout.write(
                        f"   Response length: {len(response.content)} bytes"
                    )
            else:
                self.stdout.write(
                    self.style.ERROR(
                        f"❌ {description}: {url} (Status: {response.status_code})"
                    )
                )
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f"❌ {description}: {url} - Error: {str(e)}")
            )

    def test_basic_pages(self):
        """Test basic website pages"""
        self.stdout.write("📄 Testing basic pages...")

        pages = [
            ("/", "Homepage"),
            ("/properties/", "Property List"),
            ("/contact/", "Contact Page"),
        ]

        for url, description in pages:
            self.test_url(url, description)

    def test_property_filtering(self):
        """Test property filtering functionality"""
        self.stdout.write("\n🔍 Testing property filtering...")

        filter_tests = [
            ("/properties/?type=apartment", "Filter by apartment"),
            ("/properties/?type=house", "Filter by house"),
            ("/properties/?type=villa", "Filter by villa"),
            ("/properties/?city=Ho Chi Minh", "Filter by city"),
            ("/properties/?price_range=1-3", "Filter by price range"),
        ]

        for url, description in filter_tests:
            self.test_url(url, description)

    def test_pagination(self):
        """Test pagination"""
        self.stdout.write("\n📄 Testing pagination...")

        pagination_tests = [
            ("/properties/?page=1", "First page"),
            ("/properties/?page=2", "Second page"),
        ]

        for url, description in pagination_tests:
            self.test_url(url, description)
