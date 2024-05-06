<!-- logic -->
<script>
    export let placeholder = '';
    export let widthvalue = '65';
    export let inputValue = '';
    export let maxchars = 50;
</script>

<!-- html -->
<input type="text" style="width: {widthvalue}px;" bind:value={inputValue} 
       placeholder={`${placeholder}`} maxlength={maxchars}/> 
       
<style>
    input{
        height: 15px;
    }

    input::placeholder{
        font-size: 1em;
    }
</style>