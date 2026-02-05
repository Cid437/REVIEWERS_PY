import random

# ===================== QUESTION SETS =====================
sets = {
    "A": [
        {"q": "What command creates a new Laravel project?",
         "o": ["laravel new app", "composer create-project laravel/laravel app", "php artisan new app", "npm create laravel"],
         "a": "B"},
        {"q": "Laravel follows which architecture?",
         "o": ["MVVM", "MVC", "MVP", "Microservices"],
         "a": "B"},
        {"q": "Which folder contains controllers?",
         "o": ["routes", "resources", "app/Http/Controllers", "database"],
         "a": "C"},
        {"q": "What file defines web routes?",
         "o": ["api.php", "web.php", "routes.php", "url.php"],
         "a": "B"},
        {"q": "Which command runs database migrations?",
         "o": ["php artisan migrate", "php artisan db", "php artisan make:migrate", "php artisan seed"],
         "a": "A"},
        {"q": "Which ORM does Laravel use?",
         "o": ["Doctrine", "Hibernate", "Eloquent", "ActiveRecord"],
         "a": "C"},
        {"q": "Which file stores environment variables?",
         "o": [".env", "config.php", "env.php", "settings.ini"],
         "a": "A"},
        {"q": "Which Blade syntax outputs escaped data?",
         "o": ["{!! !!}", "{{ }}", "@print", "@echo"],
         "a": "B"},
        {"q": "What command starts the Laravel dev server?",
         "o": ["php artisan serve", "npm run dev", "php serve", "laravel run"],
         "a": "A"},
        {"q": "Which folder contains Blade views?",
         "o": ["views", "resources/views", "app/views", "templates"],
         "a": "B"},
        {"q": "Which artisan command creates a controller?",
         "o": ["make:controller", "new:controller", "create:controller", "artisan controller"],
         "a": "A"},
        {"q": "Which HTTP method updates data?",
         "o": ["GET", "POST", "PUT", "FETCH"],
         "a": "C"},
        {"q": "Which command clears route cache?",
         "o": ["route:clear", "cache:clear", "clear:route", "optimize"],
         "a": "A"},
        {"q": "Which file configures database connections?",
         "o": ["database.php", "db.php", "config/database.php", ".env.db"],
         "a": "C"},
        {"q": "Which helper redirects users?",
         "o": ["redirect()", "route()", "view()", "url()"],
         "a": "A"},
        {"q": "What is Laravel Sail?",
         "o": ["Testing tool", "Docker environment", "ORM", "CLI"],
         "a": "B"},
        {"q": "Which Blade directive is for loops?",
         "o": ["@foreach", "@loop", "@forloop", "@repeat"],
         "a": "A"},
        {"q": "Which command creates a model?",
         "o": ["make:model", "new:model", "create:model", "artisan model"],
         "a": "A"},
        {"q": "Which folder stores migrations?",
         "o": ["database/migrations", "app/migrations", "resources/migrations", "storage/migrations"],
         "a": "A"},
        {"q": "Which method retrieves all records?",
         "o": ["get()", "find()", "all()", "fetch()"],
         "a": "C"},
    ],

    "B": [
        {"q": "Which command creates a migration?",
         "o": ["make:migration", "new:migration", "create:migration", "artisan migrate"],
         "a": "A"},
        {"q": "Which Blade directive checks condition?",
         "o": ["@if", "@check", "@condition", "@isset"],
         "a": "A"},
        {"q": "Which middleware handles authentication?",
         "o": ["auth", "verify", "login", "secure"],
         "a": "A"},
        {"q": "What is Laravel Sanctum used for?",
         "o": ["Views", "Authentication", "Caching", "Testing"],
         "a": "B"},
        {"q": "Which file defines API routes?",
         "o": ["api.php", "web.php", "routes.php", "rest.php"],
         "a": "A"},
        {"q": "Which artisan command creates middleware?",
         "o": ["make:middleware", "new:middleware", "create:middleware", "artisan middleware"],
         "a": "A"},
        {"q": "Which method deletes a model?",
         "o": ["remove()", "delete()", "destroy()", "drop()"],
         "a": "B"},
        {"q": "Which caching driver stores data in files?",
         "o": ["redis", "memcached", "file", "array"],
         "a": "C"},
        {"q": "Which command lists all routes?",
         "o": ["route:list", "routes:show", "route:show", "artisan routes"],
         "a": "A"},
        {"q": "Which Blade directive extends layouts?",
         "o": ["@extends", "@section", "@yield", "@include"],
         "a": "A"},
        {"q": "Which method finds a record by ID?",
         "o": ["get()", "find()", "first()", "where()"],
         "a": "B"},
        {"q": "Which Laravel feature queues jobs?",
         "o": ["Events", "Jobs", "Tasks", "Threads"],
         "a": "B"},
        {"q": "Which artisan command clears cache?",
         "o": ["cache:clear", "clear:cache", "optimize", "route:clear"],
         "a": "A"},
        {"q": "Which directory stores logs?",
         "o": ["storage/logs", "app/logs", "logs", "resources/logs"],
         "a": "A"},
        {"q": "Which method updates records?",
         "o": ["change()", "modify()", "update()", "edit()"],
         "a": "C"},
        {"q": "Which helper generates URLs?",
         "o": ["route()", "url()", "link()", "path()"],
         "a": "B"},
        {"q": "Which Laravel file handles exceptions?",
         "o": ["Handler.php", "Exception.php", "Error.php", "Catch.php"],
         "a": "A"},
        {"q": "Which Blade directive includes subviews?",
         "o": ["@include", "@extends", "@section", "@yield"],
         "a": "A"},
        {"q": "Which artisan command runs seeders?",
         "o": ["db:seed", "migrate:seed", "seed:run", "artisan seed"],
         "a": "A"},
        {"q": "Which method returns first record?",
         "o": ["first()", "get()", "find()", "one()"],
         "a": "A"},
    ],

    "C": [
        {"q": "Which Laravel feature handles background tasks?",
         "o": ["Jobs", "Routes", "Controllers", "Views"],
         "a": "A"},
        {"q": "Which Blade directive defines content section?",
         "o": ["@section", "@yield", "@extends", "@include"],
         "a": "A"},
        {"q": "Which command creates auth scaffolding?",
         "o": ["ui auth", "make:auth", "auth:make", "artisan auth"],
         "a": "B"},
        {"q": "Which file defines service providers?",
         "o": ["config/app.php", "providers.php", "services.php", "bootstrap.php"],
         "a": "A"},
        {"q": "Which HTTP status means success?",
         "o": ["200", "404", "500", "302"],
         "a": "A"},
        {"q": "Which Laravel tool handles emails?",
         "o": ["Mail", "Notify", "Postman", "Queue"],
         "a": "A"},
        {"q": "Which Blade syntax outputs raw HTML?",
         "o": ["{{ }}", "{!! !!}", "@html", "@raw"],
         "a": "B"},
        {"q": "Which command optimizes performance?",
         "o": ["optimize", "cache:run", "boost", "speed"],
         "a": "A"},
        {"q": "Which Laravel feature handles events?",
         "o": ["Listeners", "Triggers", "Hooks", "Signals"],
         "a": "A"},
        {"q": "Which file defines app key?",
         "o": [".env", "config/app.php", "key.php", "artisan"],
         "a": "A"},
        {"q": "Which method paginates results?",
         "o": ["paginate()", "limit()", "page()", "split()"],
         "a": "A"},
        {"q": "Which command creates policy?",
         "o": ["make:policy", "new:policy", "create:policy", "artisan policy"],
         "a": "A"},
        {"q": "Which feature protects routes?",
         "o": ["Middleware", "Controllers", "Views", "Models"],
         "a": "A"},
        {"q": "Which Blade directive displays errors?",
         "o": ["@error", "@errors", "@fail", "@alert"],
         "a": "A"},
        {"q": "Which Laravel tool handles scheduling?",
         "o": ["Scheduler", "Cron", "Tasker", "Timer"],
         "a": "A"},
        {"q": "Which artisan command shows version?",
         "o": ["--version", "version", "artisan version", "show:version"],
         "a": "A"},
        {"q": "Which method creates records?",
         "o": ["insert()", "create()", "make()", "new()"],
         "a": "B"},
        {"q": "Which folder stores configs?",
         "o": ["config", "settings", "env", "resources"],
         "a": "A"},
        {"q": "Which helper returns a view?",
         "o": ["view()", "render()", "display()", "show()"],
         "a": "A"},
        {"q": "Which Laravel feature secures forms?",
         "o": ["CSRF", "Auth", "Guard", "Shield"],
         "a": "A"},
    ]
}

# ===================== QUIZ FUNCTION =====================
def run_quiz():
    choice = input("\nChoose set (A / B / C): ").upper()
    if choice not in sets:
        print("Invalid set.")
        return

    questions = sets[choice][:]
    random.shuffle(questions)
    score = 0

    for i, q in enumerate(questions, 1):
        print(f"\n{i}. {q['q']}")
        for idx, opt in zip(["A", "B", "C", "D"], q["o"]):
            print(f"   {idx}. {opt}")

        ans = input("Answer: ").strip().upper()

        if ans == q["a"]:
            print("✔ Correct")
            score += 1
        else:
            correct_text = q["o"][ord(q["a"]) - 65]
            print(f"✘ Wrong — Correct answer: {q['a']}. {correct_text}")

    print(f"\nFinal Score: {score} / {len(questions)}")

# ===================== MAIN LOOP =====================
def main():
    while True:
        run_quiz()
        restart = input("\nDo you want to restart the exam? (Y/N): ").upper()
        if restart != "Y":
            print("Good luck with your Laravel studies! 👋")
            break

if __name__ == "__main__":
    main()
