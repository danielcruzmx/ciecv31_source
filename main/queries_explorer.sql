SELECT 'SADI 81' AS CONDOMINIO,
	   min(fecha_inicial) as INI,
       max(fecha_final) as FIN,
       case when c.clave_mayor = '41' then 'INGRESOS'
       		when c.clave_mayor = '51' then 'EGRESOS'
            else 'otro' end as TIPO,
       c.descripcion AS DESCRIPCION,
       sum(dm.monto) AS MONTO
FROM cuenta_contable c,
     sadiochouno_detalle_movimiento dm,
     sadiochouno_movimiento m,
     periodo p,
     condominio cn
WHERE c.id = dm.cuenta_contable_id
  AND m.fecha >= p.fecha_inicial
  AND m.fecha <= p.fecha_final
  AND dm.movimiento_id = m.id
  ANd p.condominio_id = cn.id
  AND cn.nombre = 'SADIOCHOUNO'
GROUP BY 1,
         4,
         5
ORDER BY 4 desc,
         5
