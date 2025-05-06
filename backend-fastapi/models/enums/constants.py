from enum import Enum

class RoleEnum(str, Enum):
    admin = "admin"
    mentor = "mentor"
    student = "student"

class GenreEnum(str, Enum):
    male = "male"
    female ="female"
    other = "other"
    
class Technologies(str, Enum):
    python = "python"
    javascript = "javascript"
    java = "java"
    csharp = "csharp"
    cpp = "cpp"
    php = "php"
    ruby = "ruby"
    go = "go"
    swift = "swift"
    kotlin = "kotlin"
    rust = "rust"
    typescript = "typescript"
    html = "html"
    css = "css"
    sql = "sql"