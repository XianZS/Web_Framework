# Python Web Frameworks Learning Repository

![s1](https://img.shields.io/badge/python-3.8%252B-blue)   ![s2](https://img.shields.io/badge/license-MIT-green)   ![s3](https://img.shields.io/badge/status-active-success)

​	A comprehensive Python web frameworks learning repository designed to help developers systematically learn various Python web frameworks. Each framework includes independent example code, tutorials, and best practices.

## 📚 Frameworks List

| Framework                      | Version | Difficulty | Type                 | Status        |
| ------------------------------ | ------- | ---------- | -------------------- | ------------- |
| [Flask](./Flask_Learn)         | 2.3.x   | ⭐☆☆        | Microframework       | ✅ Complete    |
| [Django](./Django_Learn)       | 4.2.x   | ⭐⭐⭐        | Full-stack Framework | 🔄 In Progress |
| [FastAPI](./FastAPI_Learn)     | 0.100.x | ⭐⭐☆        | Async Framework      | 🔄 In Progress |
| [Tornado](./Tornado_Learn)     | 6.3.x   | ⭐⭐☆        | Async Framework      | 📅 Planned     |
| [Bottle](./Bottle_Learn)       | 0.12.x  | ⭐☆☆        | Microframework       | 📅 Planned     |
| [Pyramid](./Pyramid_Learn)     | 2.0.x   | ⭐⭐☆        | Mid-level Framework  | 📅 Planned     |
| [Sanic](./Sanic_Learn)         | 23.6.x  | ⭐⭐☆        | Async Framework      | 📅 Planned     |
| [Falcon](./Falcon_Learn)       | 3.1.x   | ⭐⭐☆        | API Framework        | 📅 Planned     |
| [Starlette](./Starlette_Learn) | 0.27.x  | ⭐⭐☆        | Async Framework      | 📅 Planned     |
| [Quart](./Quart_Learn)         | 0.18.x  | ⭐⭐☆        | Async Flask          | 📅 Planned     |

## 🚀 Quick Start

### Environment Requirements
- Python 3.8+
- pip or poetry
- Git

### Installation Steps

1. Clone the repository:
```bash
git clone https://github.com/yourusername/Web_Framework.git
cd Web_Framework
```

2. Create a virtual environment (recommended):
```bash
conda create -n Web_Framework python==3.8
# Windows
conda activate Web_Framework
# Linux/Mac
conda activate Web_Framework
```

3. Install basic dependencies:
```bash
pip install -r requirements.txt
```

## 📁 Project Structure

### Root Directory
- **README.md**: Main project documentation, including framework list, quick start guide, learning path, etc.
- **LICENSE**: MIT license file
- **flask.md**: Flask framework related documentation
- **some.py**: Sample script file
- **app.c**: C language sample file
- **assets/**: Contains SVG icons and image resources used in the project

### Flask_Learn Directory
- **1_flask_use.py**: Basic Flask usage example, includes a simple Hello World application
- **2_flask_route.py**: Flask routing example, demonstrates different types of route definitions and request methods
- **3_flask_view_function.py**: Flask view function example, demonstrates request pre/post processing, status code return, etc.
- **4_flask_template_make.py**: Flask template usage example
- **5_flask_form_make.py**: Flask form handling example
- **6_flask_database.py**: Flask database operation example
- **7_flask_bp/**: Flask Blueprint example, includes modular routing and templates
- **8_flask_error_and_mid/**: Flask error handling and middleware example
- **9_flask_middleware.py**: Flask middleware usage example
- **10_bushu/**: Flask deployment example, includes NGINX configuration and Waitress server configuration
- **main.py**: Flask main application example file
- **templates/**: Contains Flask template files

### FastAPI_Learn Directory
- **1_fastapi_simple.py**: Basic FastAPI usage example, includes a simple Hello World application
- **2_FastAPI_r_s_arguments.py**: FastAPI path parameters and query parameters example
- **3_fastapi_pydantic.py**: FastAPI data model (Pydantic) example
- **4_fastapi_cookie.py**: FastAPI Cookie handling example
- **5_fastapi_header.py**: FastAPI Header handling example
- **6_form_data.py**: FastAPI form data handling example
- **7_fastapi_file.py**: FastAPI file upload example
- **8_fastapi_status_code.py**: FastAPI status code setting example
- **9_fastapi_depend_about_*.py**: FastAPI dependency injection examples, including function dependencies, class dependencies, and child dependencies
- **10_fastapi_oauth.py**: FastAPI OAuth2 authentication example
- **10_fastapi_oauth_jwt.py**: FastAPI JWT authentication example
- **11_fastapi_middleware.py**: FastAPI middleware example
- **12_fastapi_sqlmodel.py**: FastAPI SQLModel database operation example


## 📖 Learning Path

### Beginner Level (Newbie Friendly)
1. **Flask** - Simplest microframework, perfect for beginners
2. **Bottle** - Single-file framework, learn basic web concepts
3. **Basic HTTP Concepts** - Request/Response, Routing, Templates

### Intermediate Level
1. **Django** - Full-stack framework, learn MVC patterns and ORM
2. **FastAPI** - Modern async API framework
3. **Database Integration** - SQLAlchemy, Django ORM
4. **Authentication & Authorization** - JWT, OAuth2

### Advanced Level
1. **Tornado** - Asynchronous non-blocking framework
2. **Sanic** - High-performance async framework
3. **Microservices Architecture** - Distributed system design
4. **Performance Optimization** - Caching, Load balancing, Database optimization

## 🔧 Recommended Development Tools

### Editors/IDEs
- **VS Code** - Lightweight with rich Python extensions
- **PyCharm** - Professional Python IDE
- **Sublime Text** - Fast and lightweight

### Development Tools
- **Postman/Insomnia** - API testing
- **Docker** - Containerized deployment
- **Redis** - Caching service
- **Nginx** - Reverse proxy

### Databases
- **PostgreSQL** - Recommended for production
- **MySQL** - Traditional relational database
- **SQLite** - Development and testing
- **MongoDB** - NoSQL database

## 📝 Learning Recommendations

### 1. Learn in Order
Recommended learning order by difficulty:

```
Flask → Django → FastAPI → Other Frameworks
```

### 2. Practical Projects
Each framework includes:
- ✅ Basic tutorials
- ✅ Example code
- ✅ Small projects
- ✅ Best practices

### 3. Comparative Learning
Pay attention to differences when learning:
- Routing definition variations
- Template engine differences
- ORM/database operation methods
- Middleware/plugin usage

## 🎯 Learning Objectives

### Short-term Goals (1-2 months)
- [ ] Master Flask basics
- [ ] Complete a Flask blog system
- [ ] Understand RESTful API design
- [ ] Learn basic database operations

### Medium-term Goals (3-6 months)
- [ ] Master Django full-stack development
- [ ] Complete a full e-commerce project
- [ ] Learn asynchronous programming basics
- [ ] Master FastAPI development

### Long-term Goals (6-12 months)
- [ ] Understand web framework principles
- [ ] Capable of framework selection
- [ ] Master performance optimization techniques
- [ ] Learn microservices architecture

## 🤝 Contribution Guidelines

Welcome contributions to code and documentation!

1. Fork the repository
2. Create a branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Contribution Standards
- Each framework's example code should be placed in its corresponding `FrameworkName_Learn` folder
- Each framework folder should have an independent README.md
- Code must comply with PEP8 standards
- Update the main README.md table when adding new frameworks

## 📊 Progress Tracking

Use GitHub Projects to track learning progress:
- [ ] To Learn
- [ ] In Progress  
- [ ] Completed
- [ ] Needs Review

## 🔗 Related Resources

### Official Documentation
- [Flask Official Documentation](https://flask.palletsprojects.com/)
- [Django Official Documentation](https://docs.djangoproject.com/)
- [FastAPI Official Documentation](https://fastapi.tiangolo.com/)

### Learning Resources
- [Real Python](https://realpython.com)
- [Full Stack Python](https://www.fullstackpython.com/)
- [Python Web Development Guide](https://docs.python-guide.org/)

### Communities
- [Python Chinese Community](https://www.python.cn/)
- [Stack Overflow](https://stackoverflow.com/questions/tagged/python)
- [Reddit r/Python](https://www.reddit.com/r/Python/)

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## ✨ Acknowledgments

Thanks to all Python web framework developers!
Thanks to open-source community contributors!

---

**Start your Python web development journey now!** 🚀

If you have any questions or suggestions, please open an Issue or contribute code via Pull Request.

**Happy Coding!** 💻

---
*Maintainer: [XianZS]*
*Email: xianzhisen_yang@outlook.com*