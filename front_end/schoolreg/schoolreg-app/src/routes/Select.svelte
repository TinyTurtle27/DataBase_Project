<script>
    export let givenoptions = []; 
    export let widthvalue = '250';
//    export let selectedValue = '';

 //   let isOpen = false;

    // Emits a 'select' event with the chosen value when an option is clicked
//    const handleSelect = (value) => {
//        selectedValue = value; 
//        isOpen = false;
//        // Dispatch the event for the parent component to listen to
//        dispatch('select', value);
//    } 
</script>

<select class="form-select" style="width: {widthvalue}px;">
    {#each givenoptions as option}
        <option value={option}>{option}</option>
    {/each}
</select>

<style>
    .form-select {
        height: 20px;
        /* Basic styling goes here */
    }
/* Basic styling goes here */ 
</style>
