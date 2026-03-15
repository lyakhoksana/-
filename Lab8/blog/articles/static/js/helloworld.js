// 📁 articles/static/js/helloworld.js

// === Список студентов ===
var groupmates = [
    {
        "name": "Василий",
        "group": "912-2",
        "age": 19,
        "marks": [4, 3, 5, 5, 4]
    },
    {
        "name": "Анна",
        "group": "912-1",
        "age": 18,
        "marks": [3, 2, 3, 4, 3]
    },
    {
        "name": "Георгий",
        "group": "912-2",
        "age": 19,
        "marks": [3, 5, 4, 3, 5]
    },
    {
        "name": "Валентина",
        "group": "912-1",
        "age": 18,
        "marks": [5, 5, 5, 4, 5]
    },
    {
        "name": "Дмитрий",
        "group": "912-3",
        "age": 20,
        "marks": [4, 4, 4, 5, 4]
    }
];


var rpad = function(str, length) {
    str = str.toString(); // преобразование в строку
    while (str.length < length) {
        str = str + ' '; // добавление пробела в конец
    }
    return str;
};

// === Функция вывода студентов в консоль ===
var printStudents = function(students) {
    console.log(
        rpad("Имя студента", 15),
        rpad("Группа", 8),
        rpad("Возраст", 8),
        rpad("Оценки", 20)
    );
    console.log("-".repeat(55)); // разделитель

    for (var i = 0; i < students.length; i++) {
        console.log(
            rpad(students[i]['name'], 15),
            rpad(students[i]['group'], 8),
            rpad(students[i]['age'], 8),
            rpad(students[i]['marks'].join(', '), 20)
        );
    }
    console.log('\n');
};


var filterByGroup = function(students, groupName) {
    var result = []; // создаём пустой массив для результатов

    for (var i = 0; i < students.length; i++) {
        // если группа студента совпадает с искомой
        if (students[i]['group'] === groupName) {
            result.push(students[i]); // добавляем в результат
        }
    }

    return result; // возвращаем отфильтрованный массив
};


var filterByGroupModern = function(students, groupName) {
    return students.filter(function(student) {
        return student.group === groupName;
    });
};

// === Функция для вывода отфильтрованных студентов ===
var printFilteredStudents = function(groupName) {
    var filtered = filterByGroup(groupmates, groupName);

    if (filtered.length === 0) {
        console.log("Студенты в группе " + groupName + " не найдены");
        return;
    }

    console.log("\n=== Студенты группы " + groupName + " ===");
    printStudents(filtered);
};

// Ждём, пока загрузится DOM
document.addEventListener('DOMContentLoaded', function() {
    console.log("🚀 JavaScript загружен!");

    // Вывод всех студентов
    console.log("\n=== ВСЕ СТУДЕНТЫ ===");
    printStudents(groupmates);

    // Пример фильтрации: выводим студентов группы "912-2"
    printFilteredStudents("912-2");

    // Пример фильтрации: выводим студентов группы "912-1"
    printFilteredStudents("912-1");

    // Пример использования современного варианта
    var group3 = filterByGroupModern(groupmates, "912-3");
    console.log("\n=== Группа 912-3 (через filter) ===");
    printStudents(group3);
});