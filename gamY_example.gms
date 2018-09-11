SETS
	t "Description of the time set" /2000*2010/
	c "Description of consumption groups" /
		cSer "Services"
		cMan "Manifacturing"
	/
;

SINGLETON SET tEnd;

tEnd = yes$(t.val = 2010);


$GROUP G_endo
	qC['cSer',t] "Consumption"
;

$BLOCK B_consumption # I am a comment
	E_qC[c,t]$tEnd[t].. qC[c,t] =E= qC[c,t-1];
$ENDBLOCK

$FUNCTION foo({bar}):
	display {bar};
$ENDFUNCTION

@foo('baz');


$LOOP G_endo:
	display {name}.l;
$ENDLOOP

$FOR {x} in range(5):
	qC.l[c,t] += {x};
$ENDFOR

