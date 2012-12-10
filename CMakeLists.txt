project(kaboom)

cmake_minimum_required(VERSION 2.6)

find_package(Qt4 REQUIRED)

add_definitions( ${QT_DEFINITIONS} )

include_directories( 
	${QT_INCLUDE_DIR} 
	${QT_QTCORE_INCLUDE_DIR} 
	${QT_QTGUI_INCLUDE_DIR} )

qt4_wrap_cpp( kaboom_MOC
	choicepage.h
	intropage.h
	migrationpage.h
	migrationpage_p.h
	migrationtool.h
	migrationtool_p.h
	diroperations/recursivedirjob.h
	diroperations/recursivedirjob_p.h
	richradiobutton.h
	warningpage.h
	)

qt4_add_resources( kaboom_QRC resources.qrc ) 

qt4_add_translation( kaboom_QM 
      kaboom_ca.ts
      kaboom_da.ts
      kaboom_de.ts
      kaboom_es.ts
      kaboom_it.ts
      kaboom_el.ts
	  )

set( kaboom_SRCS
      kaboomsettings.cpp
      choicepage.cpp
      intropage.cpp
      main.cpp
      migrationpage.cpp
      migrationtool.cpp
      warningpage.cpp
      diroperations/diroperations.cpp
      diroperations/recursivedirjob.cpp
      diroperations/progresswidget.cpp
      richradiobutton.cpp
      kaboomlog.cpp
)

add_executable( kaboom 
	${kaboom_SRCS} 
	${kaboom_MOC} 
	${kaboom_QRC}
	${kaboom_QM}
	)

target_link_libraries( kaboom 
	${QT_QTCORE_LIBRARY} 
	${QT_QTGUI_LIBRARY} )

install( FILES ${kaboom_QM} DESTINATION share/kaboom )
install( TARGETS kaboom DESTINATION ${QT_BINARY_DIR} )
install( PROGRAMS generatedirs.sh DESTINATION ${QT_BINARY_DIR}  )

