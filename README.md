# Python Web Frameworks Learning Repository

![s1](https://img.shields.io/badge/python-3.8%252B-blue)![s2](https://img.shields.io/badge/license-MIT-green)![s3](https://img.shields.io/badge/status-active-success)

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

```
Web_Framework/
├── Flask_Learn/                 # Flask Framework Learning
│   ├── examples/               # Example Code
│   ├── tutorials/              # Tutorial Documentation
│   ├── projects/               # Complete Projects
│   └── README.md               # Flask-specific README
├── Django_Learn/               # Django Framework Learning
│   ├── projects/               # Django Projects
│   ├── apps/                   # Django Applications
│   └── README.md               # Django-specific README
├── FastAPI_Learn/              # FastAPI Framework Learning
│   ├── examples/               # Async Examples
│   ├── projects/               # Complete API Projects
│   └── README.md               # FastAPI-specific README
├── requirements.txt            # Common Dependencies
├── setup.py                    # Project Installation Configuration
├── .gitignore                  # Git Ignore Files
└── README.md                   # Main README File
```

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
