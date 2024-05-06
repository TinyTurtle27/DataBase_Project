<script>
    export let textlabel = '';
    let isChecked = false;

    import { createEventDispatcher } from 'svelte';
    const dispatch = createEventDispatcher()

    function toggleCheckbox() {
        isChecked = !isChecked;
        dispatch('update', {textlabel, isChecked});
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