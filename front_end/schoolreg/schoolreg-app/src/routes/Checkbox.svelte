<script>
    export let textlabel = '';
    let isChecked = false;

    function toggleCheckbox() {
        isChecked = !isChecked;
    }
</script>

<div class="namedcheckbox">
    <input type="checkbox" bind:checked={isChecked} on:click={toggleCheckbox}>
    <strong> <label for={textlabel}>{textlabel}</label> </strong>
</div>

<style>
    .namedcheckbox {
        display: flex;
        align-items: center;
        padding-right: 5px;
    }
</style>