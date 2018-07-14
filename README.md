# ReList

This is my implementation on a Todo list app using Vue.js for a frontend framework and flask for a backend framework.

Just a heads up...

I did somethings in this project that might seem stupid, like writing queries by hand, implemnting my own authentication system, and not using some sort of framework to write the RESTful API. This is just a project for learning and developing... not something I would do in a production setting.

I did this in 36 hours with coffee, take it for what it is.

Works like any other productivity app:

- You can create todos
- You can remove todos
- You can append todos

You are also able to attach some metadata to the todos, like:

- Due date
- Project
- Label

There are a couple different "views" to see what you need to do:

1. The "inbox" view: where you see everything
2. The "project" view where you see everything for a specific project
3. The "week" view where you see all todos with a due date within the next 7 days

