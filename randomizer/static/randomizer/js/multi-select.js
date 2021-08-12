(function($) {
    $(document).ready(function() {
        $('body').on('click', '.multiselect-select-all', function() {
            container = $(this).closest(".flag-container-list");
            container.find("input[type='checkbox']").prop('checked', true);
        })
        $('body').on('click', '.multiselect-clear-all', function() {
            container = $(this).closest(".flag-container-list");
            container.find("input[type='checkbox']").prop('checked', false);
        })
    })
})(jQuery);
