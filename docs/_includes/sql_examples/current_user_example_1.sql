SELECT
AR.grantee,
  AR.role_name,
  OP.privilege_type,
  OP.object_type,
  OP.object_name
FROM information_schema.applicable_roles AS AR
JOIN information_schema.object_privileges AS OP
ON (AR.role_name = OP.grantee)
WHERE
  AR.grantee = session_user();
