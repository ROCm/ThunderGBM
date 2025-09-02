option(ENABLE_CODE_COVERAGE                    "Enable code coverage"                          OFF)

if(MSVC)
    cmake_minimum_required(VERSION 3.4)
else()
    cmake_minimum_required(VERSION 3.21)
endif()
set(CMAKE_C_COMPILER "hipcc")
set(CMAKE_CXX_COMPILER "hipcc")
set(CMAKE_PREFIX_PATH "/opt/rocm/lib/cmake")
set(CMAKE_POLICY_VERSION_MINIMUM "3.5")
set(CMAKE_HIP_SOURCE_FILE_EXTENSIONS hip;cu)
set(CMAKE_HIP_ARCHITECTURES "gfx942")

project(thundergbm LANGUAGES CXX HIP)
find_package(HIP REQUIRED)
enable_language(HIP)
find_package(rocThrust REQUIRED) # Finds rocThrust (Thrust's HIP backend)
find_package(hipcub REQUIRED)
if(NOT hipcub_FOUND)
    message(STATUS "hipCUB could not be found, exiting")
    return(1)
endif()
include_directories(${HIP_INCLUDE_DIRS})
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} --offload-arch=gfx942")

if (NOT CMAKE_BUILD_TYPE)
    set(CMAKE_BUILD_TYPE Release)
endif ()

find_package(OpenMP REQUIRED QUIET)
if (OPENMP_FOUND)
    set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} ${OpenMP_C_FLAGS}")
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} ${OpenMP_CXX_FLAGS}")
endif ()

# for easylogging++ configuration
add_definitions("-DELPP_FEATURE_PERFORMANCE_TRACKING")
add_definitions("-DELPP_THREAD_SAFE")
add_definitions("-DELPP_STL_LOGGING")
add_definitions("-DELPP_NO_LOG_TO_FILE") 
add_definitions("-DUSE_ROCM") 
add_definitions("-D__HIP_PLATFORM_AMD__") 
add_definitions("-D__HIP__") 
# includes
include_directories(AFTER SYSTEM /opt/rocm/include)

set(COMMON_INCLUDES ${PROJECT_SOURCE_DIR}/include ${CMAKE_CURRENT_BINARY_DIR} ${HIP_INCLUDE_DIRS})
include_directories(${COMMON_INCLUDES})

add_subdirectory(src/thundergbm)

#if(ENABLE_CODE_COVERAGE)
# set(CMAKE_HIP_FLAGS "${CMAKE_HIP_FLAGS} -fprofile-instr-generate -fcoverage-mapping")
# set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -fprofile-instr-generate -fcoverage-mapping")
# set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -fprofile-instr-generate -fcoverage-mapping")
#endif()
if(ENABLE_CODE_COVERAGE)
    set(COVERAGE_FLAGS "-fprofile-instr-generate -fcoverage-mapping")
    # For ALL targets, not just tests
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} ${COVERAGE_FLAGS}")
    set(CMAKE_C_FLAGS   "${CMAKE_C_FLAGS} ${COVERAGE_FLAGS}")
    set(CMAKE_HIP_FLAGS "${CMAKE_HIP_FLAGS} ${COVERAGE_FLAGS}")
    # Also instrument linker flags (for executables)
    set(CMAKE_EXE_LINKER_FLAGS "${CMAKE_EXE_LINKER_FLAGS} ${COVERAGE_FLAGS}")
endif()

set(BUILD_TESTS ON CACHE BOOL "Build Tests")
if (BUILD_TESTS)
    add_subdirectory(src/test)
endif ()

# configuration file
set(DATASET_DIR ${PROJECT_SOURCE_DIR}/datasets/)
configure_file(include/thundergbm/config.h.in config.h)

