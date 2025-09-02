#ifndef USE_ROCM
#include "cusparse.h"
#else
    #include <rocsparse/rocsparse.h>
 #define cusparseHandle_t rocsparse_handle
    #define cusparseMatDescr_t rocsparse_mat_descr
    #define cusparseStatus_t rocsparse_status
    
    // Function mappings
    #define cusparseCreate rocsparse_create_handle
    #define cusparseDestroy rocsparse_destroy_handle
    #define cusparseSetStream rocsparse_set_stream
    #define cusparseCreateMatDescr rocsparse_create_mat_descr
    #define cusparseDestroyMatDescr rocsparse_destroy_mat_descr
    #define cusparseSetMatIndexBase rocsparse_set_mat_index_base
    #define cusparseSetMatType rocsparse_set_mat_type
    
    // Constant mappings
    #define CUSPARSE_INDEX_BASE_ZERO rocsparse_index_base_zero
    #define CUSPARSE_MATRIX_TYPE_GENERAL rocsparse_matrix_type_general
    #define CUSPARSE_ACTION_NUMERIC rocsparse_action_numeric
    
    // Operation mappings (add as needed)
    #define cusparseScsr2csc rocsparse_scsr2csc
    #define cusparseDcsr2csc rocsparse_dcsr2csc
    #define cusparseScsrmv rocsparse_scsrmv
    #define cusparseDcsrmv rocsparse_dcsrmv
#endif

