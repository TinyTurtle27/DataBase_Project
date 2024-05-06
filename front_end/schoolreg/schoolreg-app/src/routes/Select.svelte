<script>
    export let givenoptions = []; //MAKE SURE TO PASS IN AN ARRAY OF OBJECTS (key, display)
    export let selectedoption = ''; //default selected object 
    export let widthvalue = '250'; //default select component width

    $: console.log(selectedoption)
</script>

<select class="form-select" style="width: {widthvalue}px;" bind:value={selectedoption}>
    {#each givenoptions as option}
        <option value={option.key}>{option.display}</option>
    {/each}
</select>

<style>
    .form-select {
        height: 20px;
    }
</style>
