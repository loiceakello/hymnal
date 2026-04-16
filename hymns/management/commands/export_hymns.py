import sqlite3
from django.core.management.base import BaseCommand
from hymns.models import Hymn

class Command(BaseCommand):
    help = "Export hymns into a standalone hymns.db file"

    def handle(self, *args, **kwargs):
        conn = sqlite3.connect("hymns.db")
        c = conn.cursor()

        # Drop and recreate hymns table
        c.execute("DROP TABLE IF EXISTS hymns")
        c.execute("""
            CREATE TABLE hymns (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                number INTEGER UNIQUE,
                title TEXT,
                lyrics TEXT
            )
        """)

        # Insert hymns from Django
        for hymn in Hymn.objects.all():
            c.execute(
                "INSERT INTO hymns (number, title, lyrics) VALUES (?, ?, ?)",
                (hymn.number, hymn.title, hymn.lyrics)
            )

        conn.commit()
        conn.close()
        self.stdout.write(self.style.SUCCESS("Exported hymns to hymns.db"))
