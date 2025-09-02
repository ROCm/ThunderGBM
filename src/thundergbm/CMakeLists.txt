set(CMAKE_ARCHIVE_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/lib)
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/lib)
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin)

#file(GLOB SRC util/*.c* builder/*.c* objective/*.c* metric/*.c* *.c*)
# Collect C++ files
file(GLOB CPP_SRC 
    util/*.cpp
    builder/*.cpp
    objective/*.cpp
    metric/*.cpp
    *.cpp
)

# Collect CUDA/HIP files
file(GLOB CU_SRC 
    util/*.cu
    builder/*.cu
    objective/*.cu
    metric/*.cu
    *.cu
)

# Combine them
set(SRC ${CPP_SRC} ${CU_SRC})

# Mark .cu files as HIP
set_source_files_properties(
    ${CU_SRC}
    PROPERTIES
    LANGUAGE HIP
)


list(REMOVE_ITEM SRC "${CMAKE_CURRENT_LIST_DIR}/thundergbm_train.cpp")
list(REMOVE_ITEM SRC "${CMAKE_CURRENT_LIST_DIR}/thundergbm_predict.cpp")

add_library(${PROJECT_NAME} SHARED ${SRC})
find_package(rocsparse REQUIRED)
target_compile_options(${PROJECT_NAME} PRIVATE
    -Wno-unused-result
    -Wno-deprecated-declarations
)
target_link_libraries(${PROJECT_NAME} roc::rocsparse ${OpenMP_CXX_LIBRARIES})

add_executable(${PROJECT_NAME}-train thundergbm_train.cpp)
if(ENABLE_CODE_COVERAGE)
  target_compile_options(thundergbm-train PRIVATE -fprofile-instr-generate -fcoverage-mapping)
  target_link_options(thundergbm-train PRIVATE -fprofile-instr-generate -fcoverage-mapping)
endif()
target_link_libraries(${PROJECT_NAME}-train ${PROJECT_NAME})

add_executable(${PROJECT_NAME}-predict thundergbm_predict.cpp)
if(ENABLE_CODE_COVERAGE)
  target_compile_options(thundergbm-predict PRIVATE -fprofile-instr-generate -fcoverage-mapping)
  target_link_options(thundergbm-predict PRIVATE -fprofile-instr-generate -fcoverage-mapping)
endif()
target_link_libraries(${PROJECT_NAME}-predict ${PROJECT_NAME})
