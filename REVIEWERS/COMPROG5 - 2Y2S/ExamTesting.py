def laravel_exam():
    questions = [
        {
            "question": "1. What command is used to create a new Laravel project using Composer?",
            "choices": [
                "A. composer create-project laravel/laravel appname",
                "B. laravel new appname",
                "C. php artisan make:project appname",
                "D. php artisan new appname"
            ],
            "answer": "A"
        },
        {
            "question": "2. Which file contains the main application routes for web pages?",
            "choices": [
                "A. routes/api.php",
                "B. routes/web.php",
                "C. routes/console.php",
                "D. routes/app.php"
            ],
            "answer": "B"
        },
        {
            "question": "3. Which Artisan command starts the Laravel development server?",
            "choices": [
                "A. php artisan serve",
                "B. php artisan start",
                "C. php artisan run",
                "D. php artisan dev"
            ],
            "answer": "A"
        },
        {
            "question": "4. Which directory contains Laravel controllers?",
            "choices": [
                "A. app/Models",
                "B. app/Http/Controllers",
                "C. resources/views",
                "D. routes/controllers"
            ],
            "answer": "B"
        },
        {
            "question": "5. What templating engine does Laravel use?",
            "choices": [
                "A. Twig",
                "B. Blade",
                "C. Smarty",
                "D. Mustache"
            ],
            "answer": "B"
        },
        {
            "question": "6. Which command creates a controller?",
            "choices": [
                "A. php artisan make:model ControllerName",
                "B. php artisan make:controller ControllerName",
                "C. php artisan new:controller ControllerName",
                "D. php artisan create:controller ControllerName"
            ],
            "answer": "B"
        },
        {
            "question": "7. Which HTTP method is typically used to update data?",
            "choices": [
                "A. GET",
                "B. POST",
                "C. PUT",
                "D. DELETE"
            ],
            "answer": "C"
        },
        {
            "question": "8. Which file stores database configuration?",
            "choices": [
                "A. config/database.php",
                "B. .env",
                "C. database.php",
                "D. app/config.php"
            ],
            "answer": "A"
        }
    ]

    score = 0

    print("\n=== Laravel Reviewer Exam ===\n")

    for q in questions:
        print(q["question"])
        for choice in q["choices"]:
            print(choice)

        user_answer = input("Your answer (A/B/C/D): ").strip().upper()

        if user_answer == q["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! Correct answer: {q['answer']}\n")

    print("=== Exam Finished ===")
    print(f"Your Score: {score} / {len(questions)}")


if __name__ == "__main__":
    laravel_exam()
