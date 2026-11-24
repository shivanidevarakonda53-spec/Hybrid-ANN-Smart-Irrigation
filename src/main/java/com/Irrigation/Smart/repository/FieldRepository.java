
package com.Irrigation.Smart.repository;

import com.Irrigation.Smart.entity.Field;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface FieldRepository extends JpaRepository<Field, Long> {

}
