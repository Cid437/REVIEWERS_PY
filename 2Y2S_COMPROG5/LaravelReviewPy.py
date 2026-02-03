import random

def laravel_exam():
    questions = [
        {
            "question": "What command is used to create a new Laravel project using Composer?",
            "choices": [
                "A. composer create-project laravel/laravel appname",
                "B. laravel new appname",
                "C. php artisan make:project appname",
                "D. php artisan new appname"
            ],
            "answer": "A"
        },
        {
            "question": "Which file contains the main application routes for web pages?",
            "choices": [
                "A. routes/api.php",
                "B. routes/web.php",
                "C. routes/console.php",
                "D. routes/app.php"
            ],
            "answer": "B"
        },
        {
            "question": "Which Artisan command starts the Laravel development server?",
            "choices": [
                "A. php artisan serve",
                "B. php artisan start",
                "C. php artisan run",
                "D. php artisan dev"
            ],
            "answer": "A"
        },
        {
            "question": "Which directory contains Laravel controllers?",
            "choices": [
                "A. app/Models",
                "B. app/Http/Controllers",
                "C. resources/views",
                "D. routes/controllers"
            ],
            "answer": "B"
        },
        {
            "question": "What templating engine does Laravel use?",
            "choices": [
                "A. Twig",
                "B. Blade",
                "C. Smarty",
                "D. Mustache"
            ],
            "answer": "B"
        },
        {
            "question": "Which command creates a controller?",
            "choices": [
                "A. php artisan make:model ControllerName",
                "B. php artisan make:controller ControllerName",
                "C. php artisan new:controller ControllerName",
                "D. php artisan create:controller ControllerName"
            ],
            "answer": "B"
        },
        {
            "question": "Which HTTP method is typically used to update data?",
            "choices": [
                "A. GET",
                "B. POST",
                "C. PUT",
                "D. DELETE"
            ],
            "answer": "C"
        },
        {
            "question": "Which file stores database configuration?",
            "choices": [
                "A. config/database.php",
                "B. .env",
                "C. database.php",
                "D. app/config.php"
            ],
            "answer": "A"
        },
        {
            "question": "Which command runs database migrations?",
            "choices": [
                "A. php artisan migrate",
                "B. php artisan db:run",
                "C. php artisan migrate:run",
                "D. php artisan database"
            ],
            "answer": "A"
        },
        {
            "question": "Which Laravel feature maps URLs to controllers?",
            "choices": [
                "A. Views",
                "B. Routes",
                "C. Models",
                "D. Middleware"
            ],
            "answer": "B"
        },
        {
            "question": "Which folder contains Blade view files?",
            "choices": [
                "A. app/views",
                "B. resources/views",
                "C. storage/views",
                "D. public/views"
            ],
            "answer": "B"
        },
        {
            "question": "Which command creates a model?",
            "choices": [
                "A. php artisan new:model",
                "B. php artisan make:model",
                "C. php artisan create:model",
                "D. php artisan model:make"
            ],
            "answer": "B"
        },
        {
            "question": "Which file defines environment variables?",
            "choices": [
                "A. env.php",
                "B. config/env.php",
                "C. .env",
                "D. settings.env"
            ],
            "answer": "C"
        },
        {
            "question": "What does MVC stand for?",
            "choices": [
                "A. Model View Controller",
                "B. Module View Controller",
                "C. Main View Component",
                "D. Model Visual Code"
            ],
            "answer": "A"
        },
        {
            "question": "Which Laravel component handles HTTP requests?",
            "choices": [
                "A. Model",
                "B. Controller",
                "C. View",
                "D. Migration"
            ],
            "answer": "B"
        },
        {
            "question": "Which Artisan command clears application cache?",
            "choices": [
                "A. php artisan clear",
                "B. php artisan cache:clear",
                "C. php artisan config:remove",
                "D. php artisan reset"
            ],
            "answer": "B"
        },
        {
            "question": "Which HTTP method is used to delete data?",
            "choices": [
                "A. GET",
                "B. POST",
                "C. PUT",
                "D. DELETE"
            ],
            "answer": "D"
        },
        {
            "question": "Which command creates a model with migration and controller?",
            "choices": [
                "A. php artisan make:model Name -mc",
                "B. php artisan make:model Name --all",
                "C. php artisan make:model Name -mcr",
                "D. php artisan create:model Name"
            ],
            "answer": "A"
        },
        {
            "question": "What is middleware mainly used for?",
            "choices": [
                "A. Database design",
                "B. Request filtering",
                "C. UI rendering",
                "D. Data migration"
            ],
            "answer": "B"
        },
        {
            "question": "Which helper generates URLs to named routes?",
            "choices": [
                "A. url()",
                "B. asset()",
                "C. route()",
                "D. link()"
            ],
            "answer": "C"
        }
    ]

    random.shuffle(questions)
    score = 0

    print("\n=== Laravel Reviewer Exam (20 Items) ===\n")

    for i, q in enumerate(questions, start=1):
        print(f"{i}. {q['question']}")
        for choice in q["choices"]:
            print(choice)

        answer = input("Your answer (A/B/C/D): ").strip().upper()

        if answer == q["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! Correct answer: {q['answer']}\n")

    print("=== Exam Finished ===")
    print(f"Your Score: {score} / 20")


def main():
    while True:
        laravel_exam()
        restart = input("\nDo you want to restart the exam? (Y/N): ").strip().upper()
        if restart != "Y":
            print("Good luck with your Laravel studies! 👋")
            break


if __name__ == "__main__":
    main()
