Django Blog Project
This is a personal blog application built with Django, showcasing advanced Django features such as custom tags, template filters, full-text search, and third-party integration for tagging and recommendations.

Features
Tagging System: Integrated django-taggit to allow easy tagging of blog posts.
Post Recommendations: Generated recommendations based on post similarities.
Custom Template Tags and Filters: Created custom tags and filters to extend Django’s templating functionality.
SEO Optimization: Created a sitemap and RSS feed for search engine crawlers and users.
Search Engine: Integrated PostgreSQL full-text search for blog posts, including stemming and ranking of search results.
Pagination: Added pagination to the post list view to improve performance and usability.
Project Status
This project is a work in progress. While many features have been implemented and are fully functional, some advanced features have not yet been completed, including:

Switching Database to PostgreSQL: The project currently uses SQLite as the database, but the transition to PostgreSQL has not been implemented yet.
Full-Text Search: The advanced search features, such as stemming and trigram similarity, are planned but not yet fully implemented.
Search View: The search view for retrieving posts by keywords is still under development.
Setup Instructions
1. Install Python and Dependencies
Ensure you have Python 3.6+ installed. You can check your Python version by running:

bash
Copy code
python3 --version
2. Create a Virtual Environment
It is recommended to create a virtual environment for this project to manage dependencies. Run the following commands:

bash
Copy code
python3 -m venv myenv
source myenv/bin/activate  # On Windows, use 'myenv\Scripts\activate'
3. Install Required Packages
Install the dependencies from requirements.txt (if available) or manually install the necessary Django packages:

bash
Copy code
pip install django
pip install django-taggit
pip install psycopg2  # For PostgreSQL support (if you plan to use PostgreSQL)
4. Apply Migrations
Run the following command to set up the database and apply migrations:

bash
Copy code
python manage.py migrate
5. Create a Superuser
Create a superuser to access the Django admin panel:

bash
Copy code
python manage.py createsuperuser
6. Run the Development Server
Start the Django development server:

bash
Copy code
python manage.py runserver
Access the blog at http://127.0.0.1:8000/ and the admin panel at http://127.0.0.1:8000/admin/.

Future Enhancements
Implement PostgreSQL as the default database.
Complete full-text search functionality with advanced ranking and trigram similarity.
Improve the UI and add additional user features (e.g., user profiles, authentication).
License
This project is open-source and available under the MIT License.

Acknowledgments
The Django Documentation for guidance on setting up and developing with Django.
django-taggit for the tagging system integration.
