import subprocess
import sys

# Liste des bibliothèques à installer
requirements = [
    "blinker==1.8.2",
    "click==8.1.7",
    "colorama==0.4.6",
    "Flask==3.0.3",
    "flask-marshmallow==1.2.1",
    "Flask-SQLAlchemy==3.1.1",
    "greenlet==3.0.3",
    "itsdangerous==2.2.0",
    "Jinja2==3.1.4",
    "MarkupSafe==2.1.5",
    "marshmallow==3.21.3",
    "marshmallow-sqlalchemy==1.0.0",
    "packaging==24.1",
    "pymysql",  # Ajout de pymysql
    "SQLAlchemy==2.0.32",
    "typing_extensions==4.12.2",
    "Werkzeug==3.0.3"
]

def install_package(package):
    """Installe un package via pip."""
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
    except subprocess.CalledProcessError:
        print(f"Erreur lors de l'installation de {package}")

def main():
    """Installe tous les packages de la liste requirements."""
    print("Installation des dépendances...")
    for package in requirements:
        install_package(package)
    print("Installation terminée.")

if __name__ == "__main__":
    main()
