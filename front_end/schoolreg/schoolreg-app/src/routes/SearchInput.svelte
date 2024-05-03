<!-- logic -->
<script>
    export let placeholder = '';
    export let widthvalue = '55';
    let inputValue = '';
</script>

<!-- html -->
<input type="text" style="width: {widthvalue}px;" bind:value={inputValue} 
       placeholder={`${placeholder}`} /> 
       
<style>
    input{
        height: 15px;
    }

    input::placeholder{
        font-size: 0.8em;
    }
</style>