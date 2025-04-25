from django.core.management.base import BaseCommand
from django.utils import timezone
from booking.models import Show, Venue
from decimal import Decimal
import datetime

class Command(BaseCommand):
    help = 'Adds sample movies to the database'

    def handle(self, *args, **kwargs):
        # Create a sample venue first
        venue, _ = Venue.objects.get_or_create(
            name="CineMax Theater",
            defaults={
                'address': "123 Movie Street, Cinema City",
                'capacity': 200
            }
        )

        # Sample movies data
        movies = [
            {
                'title': "The Dark Knight",
                'description': "When the menace known as the Joker wreaks havoc and chaos on the people of Gotham, Batman must accept one of the greatest psychological and physical tests of his ability to fight injustice.",
                'date': timezone.now() + datetime.timedelta(days=1),
                'price': Decimal('15.99'),
                'total_seats': 100,
            },
            {
                'title': "Inception",
                'description': "A thief who steals corporate secrets through the use of dream-sharing technology is given the inverse task of planting an idea into the mind of a C.E.O.",
                'date': timezone.now() + datetime.timedelta(days=2),
                'price': Decimal('14.99'),
                'total_seats': 150,
            },
            {
                'title': "The Shawshank Redemption",
                'description': "Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.",
                'date': timezone.now() + datetime.timedelta(days=3),
                'price': Decimal('12.99'),
                'total_seats': 120,
            },
            {
                'title': "Pulp Fiction",
                'description': "The lives of two mob hitmen, a boxer, a gangster and his wife, and a pair of diner bandits intertwine in four tales of violence and redemption.",
                'date': timezone.now() + datetime.timedelta(days=4),
                'price': Decimal('13.99'),
                'total_seats': 130,
            },
            {
                'title': "The Matrix",
                'description': "A computer programmer discovers that reality as he knows it is a simulation created by machines, and joins a rebellion to break free.",
                'date': timezone.now() + datetime.timedelta(days=5),
                'price': Decimal('16.99'),
                'total_seats': 180,
            }
        ]

        for movie in movies:
            Show.objects.get_or_create(
                title=movie['title'],
                defaults={
                    'description': movie['description'],
                    'venue': venue,
                    'date': movie['date'],
                    'price': movie['price'],
                    'total_seats': movie['total_seats'],
                    'booked_seats': 0
                }
            )

        self.stdout.write(self.style.SUCCESS('Successfully added sample movies')) 