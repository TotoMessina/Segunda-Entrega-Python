from setuptools import setup, find_packages

setup(
    name="modelado_clientes",  # Nombre del paquete
    version="0.1",  # Versión del paquete
    packages=find_packages(),  # Encuentra automáticamente todos los paquetes y subpaquetes
    install_requires=[],  # Lista de dependencias que necesita el paquete, si hay alguna
    author="Tu Nombre",  # Tu nombre
    author_email="tu_email@example.com",  # Tu correo electrónico
    description="Un paquete para el modelado de clientes en una página de compras",  # Breve descripción del paquete
    long_description=open('README.md').read(),  # Descripción larga del paquete leída desde el archivo README
    long_description_content_type='text/markdown',  # Tipo de contenido de la descripción larga
    url="https://github.com/tu_usuario/modelado_clientes",  # URL del proyecto (GitHub u otro)
    classifiers=[  
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',  
)
