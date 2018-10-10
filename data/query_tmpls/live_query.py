Q_DATA_NOW = """SELECT 
    id_control_unit_data, ship_description,
    MAX_TRIP.last_record AS last_record, 
    array_states[cursor_now+1] AS act_state, state_name,
    main_event_field
    FROM states, ships
    INNER JOIN control_unit_data
    ON fk_ship = id_ship
    INNER JOIN sequences
    ON control_unit_data.fk_portinformer = sequences.fk_portinformer
    INNER JOIN (
        SELECT fk_control_unit_data,
        MAX(ts_main_event_field_val) AS last_record
        FROM trips_logs
        WHERE fk_state in {states_of_interest} 
        GROUP BY fk_control_unit_data
    ) as MAX_TRIP 
    ON MAX_TRIP.fk_control_unit_data = id_control_unit_data
    WHERE (is_active = true
    OR on_hold = true
    OR ts_archived >= CURRENT_DATE)
    AND array_states[cursor_now+1] = states.id_state
    AND array_states[cursor_now+1] in {states_of_interest}
    AND control_unit_data.fk_portinformer = {id_portinformer}
    ORDER BY id_control_unit_data;
"""

Q_DATA_ARRIVAL_PREV = """
    SELECT ts_arrival_prevision,
    ship_description 
    FROM planned_arrivals INNER JOIN ships
    ON fk_ship = id_ship
    WHERE is_active = true
    AND fk_portinformer = {id_portinformer};
"""

Q_DATA_SHIPPED_GOODS = """
    SELECT id_control_unit_data, quantity, unit, 
    ship_description, description as goods_category,
    goods_mvmnt_type 
    FROM goods_categories INNER JOIN shipped_goods 
    ON fk_goods_category  = id_goods_category
    INNER JOIN control_unit_data
    on shipped_goods.fk_control_unit_data = id_control_unit_data
    INNER JOIN ships
    ON fk_ship = id_ship
    WHERE control_unit_data.is_active = true
    AND control_unit_data.fk_portinformer = {id_portinformer}
"""


Q_DATA_TRAFFIC_LIST = """
    SELECT id_control_unit_data, 
    ship_description, num_container, num_camion, num_passengers, 
    num_furgoni, num_rimorchi, num_auto, num_moto, num_camper,
    num_bus, num_minibus, traffic_list_mvnt_type
    FROM ships INNER JOIN control_unit_data
    ON fk_ship = id_ship
    INNER JOIN traffic_list 
    ON fk_control_unit_data  = id_control_unit_data
    WHERE control_unit_data.is_active = true
    AND control_unit_data.fk_portinformer = {id_portinformer}
"""

Q_STATIC_DATA = """
    SELECT id_control_unit_data, ship_description, 
    ts_main_event_field_val
    FROM trips_logs
    INNER JOIN control_unit_data
    ON fk_control_unit_data = id_control_unit_data
    INNER JOIN ships
    ON fk_ship = id_ship
    WHERE LENGTH(ts_main_event_field_val) > 4
    AND control_unit_data.fk_portinformer = {id_portinformer}
    AND DATE(ts_main_event_field_val) = '{input_date}'
    AND fk_state in {states_of_interest}
    ORDER BY id_control_unit_data
"""
