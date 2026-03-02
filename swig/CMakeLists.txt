cmake_minimum_required(VERSION 3.10)

ADD_DEFINITIONS(-D _UNICODE)
ADD_DEFINITIONS(-D UNICODE)

ADD_DEFINITIONS(-D _CMAKE_BUILD)
IF(CMAKE_SIZEOF_VOID_P EQUAL 8)
	SET(PYTHON_HOME $ENV{PYTHON64_ROOT})
else()
	SET(PYTHON_HOME $ENV{PYTHON32_ROOT})
endif()

SET(SRC_FILES "easyop_wrap.cxx")

add_library(easyop SHARED ${SRC_FILES})

target_include_directories(easyop PUBLIC
"${PROJECT_BINARY_DIR}"
"${CMAKE_CURRENT_SOURCE_DIR}"
"${PYTHON_HOME}\\include"
)
message(STATUS "${PYTHON_HOME}\\libs")
target_link_directories(easyop PUBLIC "${PYTHON_HOME}\\libs")
#find_library(OP_LIB op ../bin/Release NO_DEFAULT_PATH)
set_target_properties(easyop PROPERTIES PREFIX "")
set_target_properties(easyop PROPERTIES OUTPUT_NAME "_easyop")
set_target_properties(easyop PROPERTIES SUFFIX ".pyd")


target_link_libraries(easyop ${op_com})

# 自动从指定 Python 根目录下的 libs 目录寻找合适的 python3X.lib
file(GLOB PYTHON_LIB_CANDIDATES "${PYTHON_HOME}/libs/python3*.lib")
if(NOT PYTHON_LIB_CANDIDATES)
  message(FATAL_ERROR "No python3*.lib found under ${PYTHON_HOME}/libs. Please check your --python*_root path.")
endif()

list(SORT PYTHON_LIB_CANDIDATES)
list(REVERSE PYTHON_LIB_CANDIDATES)
list(GET PYTHON_LIB_CANDIDATES 0 PYTHON_LIB_SELECTED)
message(STATUS "Using Python library: ${PYTHON_LIB_SELECTED}")
target_link_libraries(easyop "${PYTHON_LIB_SELECTED}")

IF(CMAKE_SIZEOF_VOID_P EQUAL 8)
  install(TARGETS easyop RUNTIME DESTINATION "${PROJECT_SOURCE_DIR}/bin/x64")
  install(TARGETS easyop ARCHIVE DESTINATION "${PROJECT_SOURCE_DIR}/lib/x64")
  install(FILES easyop.py DESTINATION "${PROJECT_SOURCE_DIR}/bin/x64")
ELSE()
  install(TARGETS easyop RUNTIME DESTINATION "${PROJECT_SOURCE_DIR}/bin/x86")
  install(TARGETS easyop ARCHIVE DESTINATION "${PROJECT_SOURCE_DIR}/lib/x86")
  install(FILES easyop.py DESTINATION "${PROJECT_SOURCE_DIR}/bin/x86")
ENDIF()
