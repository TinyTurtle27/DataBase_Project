var subjects = [
    {key: "ACCT", display: "Accounting"}, 
    {key: "ADMN", display: "Administration"},
    {key: "AS", display: "Aerospace Studies"},
    {key: "ASL", display: "American Sign Language"},
    {key: "ANTH", display: "Anthropology"},
    {key: "ARAB", display: "Arabic"},
    {key: "ART", display: "Art"},
    {key: "AAED", display: "Art Education"},
    {key: "AH", display: "Art History"},
    {key: "ASTR", display: "Astronomy"}, 
    {key: "BIOL", display: "Biology"}, 
    {key: "CAHU", display: "Cahuilla"},
    {key: "CAL", display: "C. Arts and Letters"},
    {key: "CHEM", display: "Chemistry"},
    {key: "CD", display: "Child Development"},
    {key: "CHIN", display: "Chinese"},
    {key: "COMM", display: "Communication Studies"},
    {key: "CSE", display: "Computer Science & Engineering"},
    {key: "COUN", display: "Counseling-Educational Counseling"},
    {key: "CJUS", display: "Criminal Justice"},
    {key: "DES", display: "Design"},
    {key: "ECON", display: "Economics"},
    {key: "EADM", display: "Educational Administration"},
    {key: "ECTS", display: "Education-Career and Technical Studies"},
    {key: "EDUC", display: "Education"},
    {key: "EDDL", display: "Education-Educational Leadership"},
    {key: "EELB", display: "Education-Elementary/Bilingual Education"},
    {key: "EESL", display: "Education-English Speakers other Languages"},
    {key: "ETEC", display: "Education-Instructional Technology"},
    {key: "EMAT", display: "Education-Master of Arts in Teaching"},
    {key: "EDMS", display: "Education-Multiple Subject"},
    {key: "ERDG", display: "Education-Reading Education"},
    {key: "EREH", display: "Education-Rehabilitiation Counseling"},
    {key: "EDSP", display: "Education-School Psychology"},
    {key: "ESTM", display: "Education-Sci, Tech, Engineering, Math"},
    {key: "ESEC", display: "Education-Secondary Education"},
    {key: "ESPE", display: "Education-Special Education"},
    {key: "ENG", display: "English"},
    {key: "ENTR", display: "Entrepreneurship"},
    {key: "ES", display: "Ethnic Studies"},
    {key: "FIN", display: "Finance"},
    {key: "FREN", display: "French"},
    {key: "GSS", display: "Gender and Sexuality Studies"},
    {key: "GEOG", display: "Geography"},
    {key: "GEOL", display: "Geology"},
    {key: "HSCI", display: "Health Science"},
    {key: "HIST", display: "History"},
    {key: "HON", display: "Honors"},
    {key: "HOSM", display: "Hospitality Management"},
    {key: "HD", display: "Human Development"},
    {key: "HRM", display: "Human Resource Management"},
    {key: "IST", display: "Information Systems and Tech"},
    {key: "IS", display: "Interdisciplinary Studies"},
    {key: "JAPN", display: "Japanese"},
    {key: "KINE", display: "Kinesiology"},
    {key: "KOR", display: "Korean"},
    {key: "LAS", display: "Latin American Studies"},
    {key: "LUIS", display: "Luise\u00f1o"},
    {key: "MGMT", display: "Management"},
    {key: "MKTG", display: "Marketing"},
    {key: "MATH", display: "Mathematics"},
    {key: "MILS", display: "Military Science"},
    {key: "MUS", display: "Music"},
    {key: "NSCI", display: "Natural Sciences"},
    {key: "NURS", display: "Nursing"},
    {key: "PHIL", display: "Philosophy"},
    {key: "PHYS", display: "Physics"},
    {key: "PSCI", display: "Political Science"},
    {key: "PORT", display: "Portuguese"},
    {key: "PSYC", display: "Psychology"},
    {key: "PA", display: "Public Administration"},
    {key: "SERR", display: "Serrano"},
    {key: "SSCI", display: "Social Sciences"},
    {key: "SW", display: "Social Work"},
    {key: "SOC", display: "Sociology"},
    {key: "SPAN", display: "Spanish"},
    {key: "SCM", display: "Supply Chain Management"},
    {key: "TA", display: "Theatre Arts"},
    {key: "USTD", display: "University Studies"},
    {key: "WLL", display: "World Languages and Literatures"}
]

//object arrays for text options in select elements 
var comparisons = [
    {key: "gte", display: "Is greater than or equal to"},
    {key: "lte", display: "Is less than or equal to"},
    {key: "gt", display: "Strictly greater than"}, 
    {key: "lt", display: "Strictly less than"},
    {key: "key", display: "peko"}
];

var groupings = [
    {key: "mione", display: "Must include one of these"},
    {key: "meone", display: "Must exclude one of these"},
    {key: "eonly", display: "Exclude only these"},
    {key: "ionly", display: "Include only these"}
];

var days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'];

var namefilters = [
    {key: "contains", display: "Contains"},
    {key: "doesnotcontain", display: "Does not contain"},
    {key: "isexactly", display: "Is exactly"}
];

var campuses = [
    {key: "sb", display: "San Bernardino"},
    {key: "pd", display: "Palm Desert"}
];

var instruction_methods = [
    {key: "inperson", display: "In Person"},
    {key: "online", display: "Online"},
    {key: "hybrid", display: "Hybrid"}
];

//populate select elements
function populateSelectElement(selectId, data) {
    var selectElement = document.getElementById(selectId);
    data.forEach(function(item) {
        var option = document.createElement('option');
        option.value = item.key;
        option.innerText = item.display;
        selectElement.appendChild(option);
    });

    // Add event listener
    selectElement.addEventListener('change', function(e) {
        console.log(e.target.value); //TODO: replace this with own function to handle select element change
    });
}

var selectElementsData = [ //holds id of select element and data to populate it with
    { id: 'selectedsubject', data: subjects },
    { id: 'startselectedcomparison', data: comparisons },
    { id: 'endselectedcomparison', data: comparisons },
    { id: 'selectedgrouping', data: groupings },
    { id: 'selectednamefilter', data: namefilters },
    { id: 'selectedcampus', data: campuses },
    { id: 'selectedinstructionmethod', data: instruction_methods}
];

selectElementsData.forEach(function(element) {
    populateSelectElement(element.id, element.data);
});

// Populate checkboxes
var checkboxes = document.getElementById('checkboxes');
days.forEach(day => {
    var checkbox = document.createElement('input');
    checkbox.type = 'checkbox';
    checkbox.value = day;
    checkbox.id = day;

    var label = document.createElement('label');
    label.htmlFor = day;

    var strong = document.createElement('strong');
    strong.appendChild(document.createTextNode(day));
    label.appendChild(strong);

    checkboxes.appendChild(checkbox);
    checkboxes.appendChild(label);
});

var checkedValues = []; //to store checked days
checkboxes.addEventListener('change', function(e) {
    //inside the checkboxes 'change' event listener
    var selectedDaysInput = document.getElementById('selectedDays');

    if (e.target.checked) {
        checkedValues.push(e.target.value);
    } 
    else {
        //remove from array if unchecked
        var index = checkedValues.indexOf(e.target.value); 
        if (index > -2) checkedValues.splice(index, 1); 
    }

    selectedDaysInput.value = checkedValues;
});