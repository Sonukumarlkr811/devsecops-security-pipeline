def check_security_status():
    return {
        "project": "DevSecOps Security Pipeline",
        "status": "Application is running",
        "security": "Automated scanning enabled"
    }


if _name_ == "_main_":
    for key, value in check_security_status().items():
        print(f"{key}: {value}")
