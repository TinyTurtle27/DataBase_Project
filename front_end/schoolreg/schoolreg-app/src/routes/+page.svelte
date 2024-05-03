<script>
	import coyote2 from '$lib/images/coyote2.png';
	import Select from './Select.svelte';
	import SearchInput from './SearchInput.svelte';
	import Checkbox from './Checkbox.svelte';

	//Lists for text options in Select components
	let comparisons = [
		"Is greater than or equal to",
		"Is less than or equal to",
		"Strictly greater than",
		"Strictly less than",
	];
	let groupings = [
		"Must include",
		"Must exclude",
		"Include only these",
	];
	let days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'];
	let namefilters = ['Contains', 'Does not contain', 'Is exactly'];
	let campuses = ['San Bernardino', 'Palm Desert'];
	let instruction_methods = ['In Person', 'Online', 'Hybrid'];

	//SearchInput bind vars
	let start_time = '';
	let end_time = '';
	let instructor_lastname = '';
	let course_number = '';
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

	<div class="search-form">
		<p>Start Time</p>
		<Select givenoptions={comparisons}/>
		<SearchInput bind:value={start_time} placeholder="5:00AM"/>

		<p>End Time</p>
		<Select givenoptions={comparisons}/>
		<SearchInput bind:value={end_time}  placeholder="10:00PM"/>

		<p>Days of the week</p>
		<div class="skipgrid-2">
			<Select givenoptions={groupings}/>
		</div>

		<div class="checkboxes">
			{#each days as day}
				<Checkbox textlabel={day}/>
			{/each}
		</div>

		<p>Instructor's Last Name</p>
		<div class="skipgrid-2">
			<Select givenoptions={namefilters} widthvalue='150'/>
			<SearchInput widthvalue='200' bind:value={instructor_lastname} placeholder="Howlader"/>
		</div>

		<p>Course Number</p>
		<div class="skipgrid-2">
			<SearchInput widthvalue='45' bind:value={course_number} placeholder="123456"/>
		</div>	

		<p>Campus</p>
		<div class="skipgrid-2">
			<Select givenoptions={campuses}/>
		</div>

		<p>Instruction method</p>
		<div class="skipgrid-2">
			<Select givenoptions={instruction_methods}/>
		</div>

		<div class="skipgrid-3">
			<div class="form-buttons">
				<button style="margin-right: 20px;">Clear </button>
				<button>Search</button>
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
