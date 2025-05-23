/*
 * Selling Partner API for Services
 * With the Services API, you can build applications that help service providers get and modify their service orders and manage their resources.
 *
 * OpenAPI spec version: v1
 *
 *
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen.git
 * Do not edit the class manually.
 */

package software.amazon.spapi.models.services.v1;

import com.google.gson.TypeAdapter;
import com.google.gson.annotations.JsonAdapter;
import com.google.gson.annotations.SerializedName;
import com.google.gson.stream.JsonReader;
import com.google.gson.stream.JsonWriter;
import io.swagger.v3.oas.annotations.media.Schema;
import java.io.IOException;
import java.util.Objects;

/** Error response returned when the request is unsuccessful. */
@Schema(description = "Error response returned when the request is unsuccessful.")
public class Error {
    @SerializedName("code")
    private String code = null;

    @SerializedName("message")
    private String message = null;

    @SerializedName("details")
    private String details = null;

    /** The type of error. */
    @JsonAdapter(ErrorLevelEnum.Adapter.class)
    public enum ErrorLevelEnum {
        @SerializedName("ERROR")
        ERROR("ERROR"),
        @SerializedName("WARNING")
        WARNING("WARNING");

        private String value;

        ErrorLevelEnum(String value) {
            this.value = value;
        }

        public String getValue() {
            return value;
        }

        @Override
        public String toString() {
            return String.valueOf(value);
        }

        public static ErrorLevelEnum fromValue(String input) {
            for (ErrorLevelEnum b : ErrorLevelEnum.values()) {
                if (b.value.equals(input)) {
                    return b;
                }
            }
            return null;
        }

        public static class Adapter extends TypeAdapter<ErrorLevelEnum> {
            @Override
            public void write(final JsonWriter jsonWriter, final ErrorLevelEnum enumeration) throws IOException {
                jsonWriter.value(String.valueOf(enumeration.getValue()));
            }

            @Override
            public ErrorLevelEnum read(final JsonReader jsonReader) throws IOException {
                Object value = jsonReader.nextString();
                return ErrorLevelEnum.fromValue((String) (value));
            }
        }
    }

    @SerializedName("errorLevel")
    private ErrorLevelEnum errorLevel = null;

    public Error code(String code) {
        this.code = code;
        return this;
    }

    /**
     * An error code that identifies the type of error that occurred.
     *
     * @return code
     */
    @Schema(required = true, description = "An error code that identifies the type of error that occurred.")
    public String getCode() {
        return code;
    }

    public void setCode(String code) {
        this.code = code;
    }

    public Error message(String message) {
        this.message = message;
        return this;
    }

    /**
     * A message that describes the error condition.
     *
     * @return message
     */
    @Schema(required = true, description = "A message that describes the error condition.")
    public String getMessage() {
        return message;
    }

    public void setMessage(String message) {
        this.message = message;
    }

    public Error details(String details) {
        this.details = details;
        return this;
    }

    /**
     * Additional details that can help the caller understand or fix the issue.
     *
     * @return details
     */
    @Schema(description = "Additional details that can help the caller understand or fix the issue.")
    public String getDetails() {
        return details;
    }

    public void setDetails(String details) {
        this.details = details;
    }

    public Error errorLevel(ErrorLevelEnum errorLevel) {
        this.errorLevel = errorLevel;
        return this;
    }

    /**
     * The type of error.
     *
     * @return errorLevel
     */
    @Schema(description = "The type of error.")
    public ErrorLevelEnum getErrorLevel() {
        return errorLevel;
    }

    public void setErrorLevel(ErrorLevelEnum errorLevel) {
        this.errorLevel = errorLevel;
    }

    @Override
    public boolean equals(java.lang.Object o) {
        if (this == o) {
            return true;
        }
        if (o == null || getClass() != o.getClass()) {
            return false;
        }
        Error error = (Error) o;
        return Objects.equals(this.code, error.code)
                && Objects.equals(this.message, error.message)
                && Objects.equals(this.details, error.details)
                && Objects.equals(this.errorLevel, error.errorLevel);
    }

    @Override
    public int hashCode() {
        return Objects.hash(code, message, details, errorLevel);
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append("class Error {\n");

        sb.append("    code: ").append(toIndentedString(code)).append("\n");
        sb.append("    message: ").append(toIndentedString(message)).append("\n");
        sb.append("    details: ").append(toIndentedString(details)).append("\n");
        sb.append("    errorLevel: ").append(toIndentedString(errorLevel)).append("\n");
        sb.append("}");
        return sb.toString();
    }

    /** Convert the given object to string with each line indented by 4 spaces (except the first line). */
    private String toIndentedString(java.lang.Object o) {
        if (o == null) {
            return "null";
        }
        return o.toString().replace("\n", "\n    ");
    }
}
