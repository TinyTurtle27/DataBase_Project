<script>
	import coyote2 from '$lib/images/coyote2.png';
	import Select from './Select.svelte';
	import SearchInput from './SearchInput.svelte';
	import Checkbox from './Checkbox.svelte';

	let subjects = [
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
	{key: "WLL", display: "World Languages and Literatures"}]

	//Object arrays for text options in Select components
	let comparisons = [
		{key: "gte", display: "Is greater than or equal to"},
		{key: "lte", display: "Is less than or equal to"},
		{key: "gt", display: "Strictly greater than"}, 
		{key: "lt", display: "Strictly less than"},
		{key: "key", display: "peko"}
	];

	let groupings = [
		{key: "mione", display: "Must include one of these"},
		{key: "meone", display: "Must exclude one of these"},
		{key: "eonly", display: "Exclude only these"},
		{key: "ionly", display: "Include only these"}
	];

	let days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'];

	let namefilters = [
		{key: "contains", display: "Contains"},
		{key: "doesnotcontain", display: "Does not contain"},
		{key: "isexactly", display: "Is exactly"}
	];

	let campuses = [
		{key: "sb", display: "San Bernardino"},
		{key: "pd", display: "Palm Desert"}
	];

	let instruction_methods = [
		{key: "inperson", display: "In Person"},
		{key: "online", display: "Online"},
		{key: "hybrid", display: "Hybrid"}
	];

	//Select bind vars
	let selectedsubject = '';
	let startselectedcomparison = '';
	let endselectedcomparison = '';
	let selectedgrouping = '';
	let selectednamefilter = '';
	let selectedcampus = '';
	let selectedinstructionmethod = '';

	//handeling checkboxes
	let checkedcheckboxes = [];
	function trackCheckbox({ detail }) {
		if (detail.isChecked) {
			//only reassingmnets are logged
			checkedcheckboxes = [...checkedcheckboxes, detail.textlabel]; //reasiggning checkedcheckboxes
			//checkedcheckboxes.push(detail.textlabel); //more efficient, just pushes new value but does not count as reassignment
		}
		else {
			checkedcheckboxes = checkedcheckboxes.filter(label => label !== detail.textlabel);
		}
	}

	//SearchInput bind vars
	let start_time = '';
	let end_time = '';
	let instructor_lastname = '';

	//search params
	let searchparameters = []; //empty be default

	//Handle search button click
	function handleSearchClick() {
		console.log("Search button clicked");
		
		searchparameters = [
		{key: "subject", value: selectedsubject},
		{key: "start_time", value: start_time},
		{key: "end_time", value: end_time},
		{key: "days", value: checkedcheckboxes},
		{key: "instructor_lastname", value: instructor_lastname},
		{key: "campus", value: selectedcampus},
		{key: "instruction_method", value: selectedinstructionmethod}
		];
	
		//build search query string
		let queryString = "?";
		for (let param of searchparameters) {
			if (param.value) { //filter out empty values
			queryString += `${param.key}=${encodeURIComponent(param.value)}&`; 
			}
		}
		queryString = queryString.slice(0, -1); //remove trailing '&'

    // Use queryString for making the query
    console.log("Query String:", queryString); 
	console.log(searchparameters);
	}


	$: console.log("selected subject is", selectedsubject);
	$: console.log("selected comparison is", startselectedcomparison);
	$: console.log("selected comparison is", endselectedcomparison);
	$: console.log(checkedcheckboxes);
	$: console.log(start_time);
	$: console.log(end_time);
</script>

<svelte:head>
	<title>Home</title>
	<meta name="description" content="Student registration demo" />
</svelte:head>

<section>
	<h1>
		<span class="coyote2">
			<picture>
				<img src={coyote2} alt="Welcome" />
			</picture>
		</span>

		<br/> Search for <br /> Courses
	</h1>

	<!-- Search form -->
	<div class="search-form">
		<p>Subject</p>
		<div class="skipgrid-2">
			<Select bind:selectedoption={selectedsubject} givenoptions={subjects}/>
		</div>

		<p>Start Time</p>
		<Select bind:selectedoption={startselectedcomparison} givenoptions={comparisons}/>
		<SearchInput bind:inputValue={start_time} placeholder="5:00AM" maxchars="7"/>

		<p>End Time</p>
		<Select bind:selectedoption={endselectedcomparison} givenoptions={comparisons}/>
		<SearchInput bind:inputValue={end_time}  placeholder="10:00PM" maxchars="7"/>

		<p>Days of the week</p>
		<div class="skipgrid-2">
			<Select bind:selectedoption={selectedgrouping} givenoptions={groupings}/>
		</div>

		<div class="checkboxes">
			{#each days as day}
				<Checkbox textlabel={day} on:update={trackCheckbox}/>
			{/each}
		</div>

		<p>Instructor's Last Name</p>
		<div class="skipgrid-2">
			<Select bind:selectedoption={selectednamefilter} givenoptions={namefilters} widthvalue='150'/>
			<SearchInput widthvalue='200' bind:inputValue={instructor_lastname} placeholder="Howlader"/>
		</div>

		<p>Campus</p>
		<div class="skipgrid-2">
			<Select bind:selectedoption={selectedcampus} givenoptions={campuses}/>
		</div>

		<p>Instruction method</p>
		<div class="skipgrid-2">
			<Select bind:selectedoption={selectedinstructionmethod} givenoptions={instruction_methods}/>
		</div>

		<div class="skipgrid-3">
			<div class="form-buttons">
				<button style="margin-right: 20px;">Clear </button>
				<button on:click={handleSearchClick}>Search</button>
			</div>
		</div>
	</div>
</section>

<style>
	.search-form {
		display: grid;
		grid-template-columns: 1fr 1fr 1fr;
		grid-template-rows: 25px 25px 25px 25px 25px 25px 25px 25px 25px;
		grid-gap: 5px;
		align-items: center;
	}

	.search-form p {
		justify-self: end;
		padding: 5px;
	}

	.search-form .checkboxes {
		display: flex;
		flex-direction: row;
		grid-column: 2 / span 2;
	}

	.form-buttons {
		display: flex;
		flex-direction: row;
		justify-content: flex-end;
	}

	.search-form .skipgrid-2 {
		grid-column-end: span 2;
	}

	.search-form .skipgrid-3 {
		grid-column-end: span 3;
	}

	section {
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
		flex: 0.6;
	}

	h1 {
		width: 100%;
	}

</style>
